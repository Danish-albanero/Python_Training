from pydeequ.analyzers import *

OPERATION_MAPPINGS = {"eq": "==", "lt": "<", "gt": ">"}


def generateFilters(filters):
    result = ""
    conditions = filters["conditions"]
    relationships = filters["relationships"]

    arr_length = len(conditions)
    for idx, condition in enumerate(conditions):
        result += f"{condition['column']}{OPERATION_MAPPINGS[condition['operation'].lower()]}'{condition['value']}'"

        if idx != arr_length - 1:
            result += f" {relationships[idx].lower()} "

    return result


def processResults(analyzerParams, analysisResults):
    result = []
    for analyzer in analyzerParams:
        if analyzer["operation"].lower() == "Histogram".lower():
            response = list(
                filter(
                    lambda x: x["name"].lower().startswith("histogram.abs")
                    and x["instance"].lower() == analyzer["column"][0].lower(),
                    analysisResults,
                )
            )

            updatedResponse = {
                "entity": response[0]["entity"],
                "instance": response[0]["instance"],
                "name": "Histogram",
                "histogram": list(
                    map(
                        lambda x: {
                            "class": "".join(x["name"].split(".")[2:]),
                            "occurrences": int(x["value"]),
                        },
                        response,
                    )
                ),
            }

            result.append(updatedResponse)
        elif analyzer["operation"].lower() == "Quantiles".lower():

            response = list(
                filter(
                    lambda x: x["name"].lower().startswith("approxquantiles")
                    and x["instance"].lower() == analyzer["column"][0].lower(),
                    analysisResults,
                )
            )

            updatedResponse = {
                "entity": response[0]["entity"],
                "instance": response[0]["instance"],
                "name": "Quantiles",
                "Quantiles": list(
                    map(
                        lambda x: {
                            "quantile": x["name"].split("-")[-1],
                            "value": float(x["value"]),
                        },
                        response,
                    )
                ),
            }

            result.append(updatedResponse)
        else:

            response = list(
                filter(
                    lambda x: x["name"].lower() == analyzer["operation"].lower()
                    and x["instance"].lower()
                    == ",".join(analyzer["column"]).lower(),
                    analysisResults,
                )
            )

            result.append(response[0])

    return result


def run_analyzer(spark, df, ops=[]):

    if len(df.head(1)) == 0:
        return []

    analysisResult = AnalysisRunner(spark).onData(df)

    hist_present = False
    for analyser in ops:
        operation, column = analyser["operation"], analyser["column"]

        if operation.lower() == "Mean".lower():
            analysisResult = analysisResult.addAnalyzer(Mean(column[0]))
        elif operation.lower() == "ApproxCountDistinct".lower():
            analysisResult = analysisResult.addAnalyzer(
                ApproxCountDistinct(column[0])
            )
        elif operation.lower() == "Distinctness".lower():
            analysisResult = analysisResult.addAnalyzer(Distinctness(column))
        elif operation.lower() == "Uniqueness".lower():
            analysisResult = analysisResult.addAnalyzer(Uniqueness(column))
        elif operation.lower() == "UniqueValueRatio".lower():
            analysisResult = analysisResult.addAnalyzer(
                UniqueValueRatio(column)
            )
        elif operation.lower() == "Histogram".lower():
            hist_present = True
            if len(analyser["filters"]["conditions"]) != 0:
                filters = generateFilters(analyser["filters"])
            else:
                filters = None

            if analyser["maxBins"] == 0:
                analyser["maxBins"] = None

            analysisResult = analysisResult.addAnalyzer(
                Histogram(
                    column[0],
                    # clips bottom records, if "number of bins" is provided
                    maxDetailBins=analyser["maxBins"],
                    where=filters,
                )
            )
        elif operation.lower() == "Correlation".lower():
            analysisResult = analysisResult.addAnalyzer(
                Correlation(column[0], column[1])
            )
        elif operation.lower() == "Quantiles".lower():
            hist_present = True
            analysisResult = analysisResult.addAnalyzer(
                ApproxQuantiles(column[0], [0.01, 0.25, 0.5, 0.75, 0.99])
            )

    analysisResult = analysisResult.run()
    analysisResult_json = AnalyzerContext.successMetricsAsJson(
        spark, analysisResult
    )

    if hist_present:
        analysisResult_json = processResults(ops, analysisResult_json)

    return analysisResult_json

import pandas as pd

from src.metrics import calculate_group_metrics, calculate_lift
from src.statistical_tests import run_all_ab_tests


def main():
    input_path = "data/raw/ab_visual_assets.csv"
    metrics_output_path = "data/processed/group_metrics.csv"
    tests_output_path = "data/processed/statistical_test_results.csv"

    df = pd.read_csv(input_path)

    summary = calculate_group_metrics(
        df=df,
        group_col="image_type"
    )

    lift = calculate_lift(
        summary_df=summary,
        treatment_group="lifestyle",
        control_group="studio"
    )

    test_results = run_all_ab_tests(
        df=df,
        group_col="image_type",
        group_a="lifestyle",
        group_b="studio"
    )

    summary.to_csv(metrics_output_path)
    test_results.to_csv(tests_output_path, index=False)

    print("Group metrics:")
    print(summary)

    print("\nLift:")
    for metric, value in lift.items():
        print(f"{metric}: {value:.2%}")

    print("\nStatistical test results:")
    print(test_results)

    print("\nFiles saved:")
    print(f"- {metrics_output_path}")
    print(f"- {tests_output_path}")


if __name__ == "__main__":
    main()
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind


def run_proportion_test(df, group_col, metric_col, group_a, group_b):
    """
    Runs a two-proportion Z-test between two independent groups.

    Parameters:
        df: pandas DataFrame
        group_col: column used to split groups
        metric_col: binary metric column, such as clicks or converted
        group_a: first group name
        group_b: second group name

    Returns:
        Dictionary with test results.
    """

    group_a_data = df[df[group_col] == group_a]
    group_b_data = df[df[group_col] == group_b]

    count = [
        group_a_data[metric_col].sum(),
        group_b_data[metric_col].sum()
    ]

    nobs = [
        group_a_data[metric_col].count(),
        group_b_data[metric_col].count()
    ]

    stat, p_value = proportions_ztest(
        count=count,
        nobs=nobs,
        alternative="two-sided"
    )

    return {
        "metric": metric_col,
        "group_a": group_a,
        "group_b": group_b,
        "group_a_value": float(group_a_data[metric_col].mean()),
        "group_b_value": float(group_b_data[metric_col].mean()),
        "test": "Two-proportion Z-test",
        "statistic": float(stat),
        "p_value": float(p_value),
        "significant": bool(p_value < 0.05)
    }

def run_t_test(df, group_col, metric_col, group_a, group_b):
    """
    Runs Welch's t-test between two independent groups.

    Parameters:
        df: pandas DataFrame
        group_col: column used to split groups
        metric_col: continuous metric column, such as time_on_page or purchase_value
        group_a: first group name
        group_b: second group name

    Returns:
        Dictionary with test results.
    """

    group_a_data = df[df[group_col] == group_a][metric_col]
    group_b_data = df[df[group_col] == group_b][metric_col]

    stat, p_value = ttest_ind(
        group_a_data,
        group_b_data,
        equal_var=False
    )

    return {
        "metric": metric_col,
        "group_a": group_a,
        "group_b": group_b,
        "group_a_value": float(group_a_data.mean()),
        "group_b_value": float(group_b_data.mean()),
        "test": "Welch's t-test",
        "statistic": float(stat),
        "p_value": float(p_value),
        "significant": bool(p_value < 0.05)
    }


def run_all_ab_tests(df, group_col, group_a, group_b):
    """
    Runs all A/B tests used in this project.

    Parameters:
        df: pandas DataFrame
        group_col: column used to split groups
        group_a: first group name
        group_b: second group name

    Returns:
        pandas DataFrame with all test results.
    """

    results = [
        run_proportion_test(
            df=df,
            group_col=group_col,
            metric_col="clicks",
            group_a=group_a,
            group_b=group_b
        ),
        run_proportion_test(
            df=df,
            group_col=group_col,
            metric_col="converted",
            group_a=group_a,
            group_b=group_b
        ),
        run_t_test(
            df=df,
            group_col=group_col,
            metric_col="time_on_page",
            group_a=group_a,
            group_b=group_b
        ),
        run_t_test(
            df=df,
            group_col=group_col,
            metric_col="purchase_value",
            group_a=group_a,
            group_b=group_b
        )
    ]

    return pd.DataFrame(results)



if __name__ == "__main__":
    df = pd.read_csv("data/raw/ab_visual_assets.csv")

    results = run_all_ab_tests(
        df=df,
        group_col="image_type",
        group_a="lifestyle",
        group_b="studio"
    )

    print(results)
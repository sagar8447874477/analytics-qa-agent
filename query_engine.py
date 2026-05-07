def generate_sql(question):

    q = question.lower()

    # DAU
    if "dau" in q:

        return """
        SELECT session_date,
        COUNT(DISTINCT user_id) as dau
        FROM sessions
        GROUP BY session_date
        ORDER BY session_date
        """

    # MAU
    elif "mau" in q:

        return """
        SELECT COUNT(DISTINCT user_id) as mau
        FROM sessions
        """

    # US USERS
    elif "us users" in q:

        return """
        SELECT COUNT(*) as total_users
        FROM users
        WHERE country='US'
        """

    # REVENUE
    elif "revenue" in q:

        return """
        SELECT SUM(amount) as revenue
        FROM transactions
        """

    # THIS WEEK VS LAST WEEK
    elif "this week vs last week" in q:

        return """
        SELECT
        CASE
            WHEN session_date >= date('now', '-7 day')
            THEN 'This Week'
            ELSE 'Last Week'
        END as week_group,
        COUNT(DISTINCT user_id) as users
        FROM sessions
        WHERE session_date >= date('now', '-14 day')
        GROUP BY week_group
        """

    # RETENTION
    elif "retention" in q:

        return """
        SELECT country,
        COUNT(DISTINCT user_id) as retained_users
        FROM users
        GROUP BY country
        """

    # AMBIGUOUS
    else:
        return None
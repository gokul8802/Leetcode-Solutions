# Write your MySQL query statement below
    (select 
        U.name as results
    from 
        MovieRating MR
    join Users U 
        on MR.user_id = U.user_id
    group by U.user_id, U.name
    order by count(MR.movie_id) desc, U.name
    limit 1)
union all
    (select 
        M.title as results
    from 
        MovieRating MR
    join Movies M on MR.movie_id = M.movie_id
        and date_format(MR.created_at,'%Y-%m') = '2020-02'
    group by MR.movie_id, M.title
    order by 
            avg(MR.rating) desc, M.title
    limit 1);
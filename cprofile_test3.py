import cProfile
import asyncio
import pstats
from task3 import main

with cProfile.Profile() as pr:
    asyncio.run(main())

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
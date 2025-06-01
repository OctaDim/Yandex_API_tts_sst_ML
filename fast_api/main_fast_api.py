from fastapi import FastAPI

# from apps.auth_token.controllers_auth_token import (
#     auth_token_router)
# from apps.calls_list.controllers_calls_list import (
#     calls_list_router)
# from apps.calls_online.controllers_calls_online import (
#     calls_online_router)
# from apps.calls_statistic.controllers_calls_stats import (
#     calls_stats_router)


app = FastAPI()

# app.include_router(auth_token_router)
# app.include_router(calls_list_router)
# app.include_router(calls_online_router)
# app.include_router(calls_stats_router)

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

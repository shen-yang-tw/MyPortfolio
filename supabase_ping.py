import os
import requests
import json
from datetime import datetime

def send_supabase_ping():
    # 1. 從環境變數中讀取 Supabase 連線資訊
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if not supabase_url or not supabase_key:
        print("[錯誤] 找不到完整的 Supabase 環境變數設定。")
        return

    # 組合完整的 REST API 寫入網址
    api_url = f"{supabase_url}/rest/v1/contact_messages"
    
    # 2. 設定符合 Supabase 規範的標準 API 標頭
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }

    # ========================================================
    # 核心修正：徹底拔除在 Python 執行 DELETE 的不穩定流程！
    # 清理舊資料的工作，完全交給我們之前在 Supabase 設好的 Trigger 去自動執行。
    # ========================================================

    # ========================================================
    # 步驟 B：寫入當下最新的一筆系統 Ping 資料
    # ========================================================
    from datetime import timedelta
    
    taiwan_time = datetime.utcnow() + timedelta(hours=8)
    current_time = taiwan_time.strftime("%Y-%m-%d %H:%M:%S")
    
    payload = {
        "name": "System_Auto_Ping",
        "email": "system@portfolio.internal",
        "message": f"此為自動發送的資料庫防休眠啟用活動。最新發送時間（台灣時間）：{current_time}"
    }
    
    try:
        print("[開始] 正在寫入最新的系統 Ping 資料...")
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
        if response.status_code in (200, 201):
            print(f"[寫入成功] 成功刺激資料庫活動！最新台灣時間：{current_time}")
        else:
            print(f"[警告] 寫入未成功，狀態碼: {response.status_code}, 回傳內容: {response.text}")
            
    except Exception as e:
        print(f"[系統錯誤] 執行寫入時連線至 Supabase 失敗: {str(e)}")

if __name__ == "__main__":
    send_supabase_ping()

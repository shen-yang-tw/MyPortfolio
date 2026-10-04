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

    # 組合完整的 REST API 網址
    api_url = f"{supabase_url}/rest/v1/contact_messages"
    
    # 2. 設定符合 Supabase 規範的標準 API 標頭
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    # ========================================================
    # 步驟 A：先清除舊的系統 Ping 留言，確保永遠不佔用空間！
    # ========================================================
    delete_url = f"{api_url}?name=eq.System_Auto_Ping"
    
    try:
        print("[開始] 正在清理資料庫中的舊系統紀錄...")
        delete_response = requests.delete(delete_url, headers=headers)
        
        # 💡 狀態碼是 200 或 204，代表刪除成功，200代表已完成任務，204代表資料已刪除且沒有任何資料回傳
        if delete_response.status_code in (200, 204):
            print("[清理成功] 舊的系統 Ping 資料已全數移除。")
        else:
            print(f"[提示] 未能完全清除舊資料（可能原本就沒資料），狀態碼: {delete_response.status_code}")
            
    except Exception as e:
        print(f"[系統錯誤] 執行清理舊資料時連線失敗: {str(e)}")


    # ========================================================
    # 步驟 B：寫入當下最新的一筆系統 Ping 資料，強制刷存在感！
    # ========================================================
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {
        "name": "System_Auto_Ping",
        "email": "system@portfolio.internal",
        "message": f"此為自動發送的資料庫防休眠啟用活動。最新發送時間：{current_time}"
    }
    
    try:
        print("[開始] 正在寫入最新的系統 Ping 資料...")
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
        # 💡 狀態碼是 200 或 201，代表寫入成功，200代表已完成任務，201代表已創建新資源
        if response.status_code in (200, 201):
            print(f"[寫入成功] 成功刺激資料庫活動！最新時間：{current_time}")
        else:
            print(f"[警告] 寫入未成功，狀態碼: {response.status_code}, 回傳內容: {response.text}")
            
    except Exception as e:
        print(f"[系統錯誤] 執行寫入時連線至 Supabase 失敗: {str(e)}")

if __name__ == "__main__":
    send_supabase_ping()

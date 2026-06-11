import asyncio
import aiohttp

usernames = [
    "x_v", "k_v", "l_w", "m_z", "n_x",
    "x_q", "k_w", "l_x", "m_q", "n_v",
    "Byv", "Cwx", "Dqz", "Fxv", "Gwz",
    "Bwz", "Cxv", "Dzw", "Fvz", "Gqx",
    "Bvz", "Cvz", "Dwx", "Fzq", "Gxv",
    "Bqz", "Cwz", "Dxz", "Fqv", "Gvw",
    "b_y", "c_w", "d_q", "f_x", "g_w",
    "b_w", "c_x", "d_z", "f_v", "g_q",
    "b_v", "c_v", "d_w", "f_z", "g_x",
    "b_q", "c_z", "d_x", "f_q", "g_v",
    "Pyz", "Rqw", "Sxv", "Twz", "Uvx",
    "Pwz", "Rxv", "Szw", "Tvz", "Uqx",
    "Pvz", "Rvz", "Swx", "Tzq", "Uxv",
    "Pqz", "Rwz", "Sxz", "Tqv", "Uvw",
    "p_y", "r_q", "s_x", "t_w", "u_v",
    "p_w", "r_x", "s_z", "t_v", "u_q",
    "p_v", "r_v", "s_w", "t_z", "u_x",
    "p_q", "r_z", "s_x", "t_q", "u_w",
    "Ayv", "Ewx", "Iqz", "Oxv", "Uwz",
    "Awz", "Exv", "Izw", "Ovz", "Uqx",
    "Avz", "Evz", "Iwx", "Ozq", "Uxv",
    "Aqz", "Ewz", "Ixz", "Oqv", "Uvw",
    "a_y", "e_w", "i_q", "o_x", "u_z",
    "a_w", "e_x", "i_z", "o_v", "u_q",
    "a_v", "e_v", "i_w", "o_z", "u_x",
    "a_q", "e_z", "i_x", "o_q", "u_w",
    "Zyv", "Qwx", "Vxr", "Jkv", "Xqw",
    "Zwx", "Qxv", "Vrx", "Jxw", "Zrv",
    "Zpx", "Qrv", "Vzx", "Jvx", "Zvw",
    "Zqx", "Qwv", "Wxv", "Jzw", "Zxw",
    "z_y", "q_x", "v_r", "j_k", "x_w",
    "z_x", "q_v", "v_x", "j_w", "x_r",
    "z_p", "q_r", "v_z", "j_v", "x_v",
    "z_q", "q_w", "w_x", "j_z", "x_z",
    "Hyz", "Hyv", "Hyw", "Hyx", "Hyq",
    "h_y", "h_z", "h_v", "h_w", "h_x",
    "Tyz", "Tyv", "Tyw", "Tyx", "Tyq",
    "t_y", "t_z", "t_v", "t_w", "t_x",
    "Syz", "Syv", "Syw", "Syx", "Syq",
    "s_y", "s_z", "s_v", "s_w", "s_x",
    "l_y", "l_z", "l_v", "l_w", "l_x",
]



async def check_username(session, username, semaphore, retries=3):
    async with semaphore:
        url = f"https://api.mojang.com/minecraft/profile/lookup/name/{username}"
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"TAKEN -> {username}")
                elif response.status == 404:
                    print(f"AVAILABLE -> {username}")
                elif response.status == 429:
                    if retries > 0:
                        await asyncio.sleep(5)
                        await check_username(session, username, semaphore, retries - 1)
                    else:
                        print(f"GAVE UP -> {username}")
                else:
                    print(f"ERROR {response.status} -> {username}")
        except asyncio.TimeoutError:
            print(f"TIMEOUT -> {username}")
        except Exception as e:
            print(f"ERROR -> {username}: {e}")

async def check_all(usernames):
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        tasks = [check_username(session, name, semaphore) for name in usernames]
        await asyncio.gather(*tasks)

asyncio.run(check_all(usernames))
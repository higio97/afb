import os

api_id = int(os.environ.get("API_ID", "WAJIB_DIISI"))
api_hash = os.environ.get("API_HASH", "WAJIB_DIISI")
bot_token = os.environ.get("BOT_TOKEN", "WAJIB_DIISI")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb://localhost:27017")
db_name = os.environ.get("DB_NAME", "telegram") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "WAJIB_DIISI"))
channel_2 = int(os.environ.get("CHANNEL_2", "WAJIB_DIISI")) #untuk group comentar user
channel_log = int(os.environ.get("CHANNEL_LOG", "WAJIB_DIISI"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "WAJIB_DIISI"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#AlterGirl #AlterBoy #AlterAsk #AlterFind #AlterSpill #AlterStory").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/ee4e4864bc4ebfb7819be.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/2562988d57d7f61384f24.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", "Hai {fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#AlterBoy / #AlterGirl untuk Mencari Pasangan, Teman , Partner FWB
#AlterAsk untuk Bertanya
#AlterStory untuk Berbagi Cerita
#AlterSpill untuk Spill Masalah
#AlterFind untuk Mencari Pasangan, Teman, Partner FWB
""")
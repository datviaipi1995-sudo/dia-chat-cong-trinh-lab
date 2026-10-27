"""Tính các chỉ tiêu vật lý và phân loại đất từ kết quả thí nghiệm trong phòng.

Chạy: python3 scripts/tinh_chi_tieu.py data/lab_samples.csv
"""
import csv
import sys

GAMMA_W = 10.0  # kN/m3


def do_deo(ip):
    if ip <= 7:
        return "Cát pha"
    if ip <= 17:
        return "Sét pha"
    return "Sét"


def trang_thai(il):
    if il <= 0:
        return "Cứng"
    if il <= 0.25:
        return "Nửa cứng"
    if il <= 0.5:
        return "Dẻo cứng"
    if il <= 0.75:
        return "Dẻo mềm"
    if il <= 1.0:
        return "Dẻo chảy"
    return "Chảy"


def tinh(row):
    w = float(row["w_pct"]) / 100
    gamma = float(row["gamma_kNm3"])
    gs = float(row["Gs"])
    ll, pl = float(row["LL_pct"]), float(row["PL_pct"])

    gamma_d = gamma / (1 + w)
    e = gs * GAMMA_W / gamma_d - 1
    n = e / (1 + e)
    sr = w * gs / e
    ip = ll - pl
    il = (w * 100 - pl) / ip
    return {
        "gamma_d": gamma_d, "e": e, "n": n, "Sr": sr,
        "IP": ip, "IL": il,
        "loai_theo_IP": do_deo(ip), "trang_thai": trang_thai(il),
    }


def main(path):
    print(f"{'Mẫu':8}{'Độ sâu':>7}{'γd':>7}{'e':>7}{'n':>7}{'Sr':>7}{'IP':>7}{'IL':>7}  {'Tên đất':10}{'Trạng thái'}")
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            r = tinh(row)
            print(f"{row['sample']:8}{float(row['depth_m']):7.1f}{r['gamma_d']:7.2f}{r['e']:7.3f}"
                  f"{r['n']:7.3f}{r['Sr']:7.2f}{r['IP']:7.1f}{r['IL']:7.2f}  "
                  f"{r['loai_theo_IP']:10}{r['trang_thai']}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/lab_samples.csv")

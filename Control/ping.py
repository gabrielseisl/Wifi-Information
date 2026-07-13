import subprocess
import re


def ping(endereco):
    try:
        resultado = subprocess.check_output(
            ["ping", endereco, "-n", "4"],
            text=True,
            encoding="cp850"
        )

        tempos = re.findall(r"tempo[=<](\d+)ms", resultado)

        if tempos:
            tempos = list(map(int, tempos))
            media = sum(tempos) / len(tempos)
        else:
            media = None

        return {
            "sucesso": True,
            "endereco": endereco,
            "media_ms": media,
            "resultado": resultado
        }

    except subprocess.CalledProcessError:
        return {
            "sucesso": False,
            "endereco": endereco,
            "media_ms": None,
            "resultado": "Não foi possível realizar o ping."
        }

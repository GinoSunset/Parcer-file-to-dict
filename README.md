Parcer file to dict
========
Предназначен для парсинга и отправки данных в бд файлов с набором данных типа ключ-значение, ключ от значения отделен двоеточием. Имеется возможность вводить многострочные значения ключа, для этого достаточно или на следующей строке продолжить значения или повторить ключ. 
В файле могут присутствовать множество документов (словарей). Для этого необходимо между документами оставить пустую строку (или несколько)
Можно оставлять комментарии. Комментарии считаются строки начинающиеся с символа решетки `#`

Пример файла:
```
#
# The contents of this file are subject to 
# AFRINIC Database Terms and Conditions
#
# http://www.afrinic.net/en/services
#

as-block:       AS30720 - AS30979
type:           REGULAR
descr:          RIPE NCC ASN block
remarks:        These AS Numbers are further assigned to network
                operators in the RIPE NCC service region. AS
                assignment policy is documented in:
                <http://www.ripe.net/ripe/docs/asn-assignment.html>
                RIPE NCC members can request AS Numbers using the
                form located at:
                <http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>
remarks:        data has been transferred from RIPE Whois Database 20050221
org:            ORG-AFNC1-AFRINIC
admin-c:        TEAM-AFRINIC
tech-c:         TEAM-AFRINIC
mnt-by:         AFRINIC-HM-MNT
mnt-lower:      AFRINIC-HM-MNT
changed:        ***@ripe.net 20031001
changed:        ***@ripe.net 20040421
changed:        ***@ripe.net 20050202
changed:        ***@afrinic.net 20050205
source:         AFRINIC
```
Пример документа после парсинга:
```python
{
        "as-block": "AS30720 - AS30979",
        "type": "REGULAR",
        "descr": "RIPE NCC ASN block",
        "remarks": "These AS Numbers are further assigned to network\n"
        "operators in the RIPE NCC service region. AS\n"
        "assignment policy is documented in:\n"
        "<http://www.ripe.net/ripe/docs/asn-assignment.html>\n"
        "RIPE NCC members can request AS Numbers using the\n"
        "form located at:\n"
        "<http://lirportal.ripe.net/lirportal/liruser/resource_request/draw.html?name=as-number>\n"
        "data has been transferred from RIPE Whois Database 20050221",
        "org": "ORG-AFNC1-AFRINIC",
        "admin-c": "TEAM-AFRINIC",
        "tech-c": "TEAM-AFRINIC",
        "mnt-by": "AFRINIC-HM-MNT",
        "mnt-lower": "AFRINIC-HM-MNT",
        "changed": "***@ripe.net 20031001\n"
        "***@ripe.net 20040421\n"
        "***@ripe.net 20050202\n"
        "***@afrinic.net 20050205",
        "source": "AFRINIC",
}
```
parse_file
---------------
Функция отвечающая за парсинг

На вход принимает вход до файла с документами. Может быть как текстовый так и сжатым gzip.
При парсинге:
* из значений будут удалены лишние пробелы
* многострочные значения объеденины в одну строку с сохранением переносов (но не отступов)
* удалены комментарии 
* ключ ищется в строке вначале которой нет пробельных символов и в строке где символы разделены символом `:`


Тестирование
---------------
Для тестирования необходимо установить `pytest` и запустить тестирование 
```
pip install -r requirements-dev.txt
python -m pytest -v
```

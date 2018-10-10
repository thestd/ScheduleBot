from robobrowser import RoboBrowser
import config.settings as stng
import io, re, json


class ScheduleScrapper:
    """
    """
    def __init__(self):
        self.browser = RoboBrowser(history=False, parser='lxml')

    def _get_page_with_schedule(self, group=None, sdate=None, edate=None, teacher=None) -> list:
        """
        This function find schedule for group
        :param group: A group for which search will be done
        :param sdate: Start date to search
        :param edate: End date to search
        :return: List of days with schedule
        """
        self.browser.open(stng.SCHEDULE_URL+stng.GET_SCHEDULE_URL)
        form = self.browser.get_forms()[0]

        if group:
            form['group'].value = group.encode(stng.DEFAULT_ENCODING_FOR_REQUEST)

        if teacher:
            form['teacher'].value = teacher.encode(stng.DEFAULT_ENCODING_FOR_REQUEST)

        if sdate:
            form['sdate'].value = sdate.encode(stng.DEFAULT_ENCODING_FOR_REQUEST)

        if edate:
            form['edate'].value = edate.encode(stng.DEFAULT_ENCODING_FOR_REQUEST)

        self.browser.submit_form(form)
        soup = self.browser.parsed
        list_of_couples = soup.find_all('div', class_='col-md-6')[1:]
        return list_of_couples

    def _parse_schedule(self, list_of_couples: list, group=None, teacher=None) -> list:
        """
        This function parse list of html tags to normal text list
        :param list_of_couples: list with html tags
        :return: list with formatting text
        """
        if group:
            appeal = f'для групи {group}'
        else:
            appeal = f'для {teacher}'
        result = list()
        for elem in list_of_couples:
            date = elem.find('h4').text
            # result.append(f'Розклад на {date}\n')
            result_str = f'<strong>Розклад на {date}\n{appeal}</strong>\n'
            for i in elem.find_all('tr'):
                pair = i.find_all('td')
                if pair[2].text != '':
                    pair_info = re.sub(" +", " ", pair[2].text)
                    pair_time = f'\n{pair[0].text} пара ({pair[1].text[:5]} - {pair[1].text[5:]})'
                    result_str += f'<i>{pair_time}</i>\n{pair_info}\n'
                    continue
            result.append(result_str)
        return result

    def _get(self, link: str, query: str) -> list:
        self.browser.open(link+query)
        response = self.browser.response.content.decode(stng.DEFAULT_ENCODING_FOR_REQUEST)
        try:
            return json.load(io.StringIO(response))["suggestions"]
        except:
            return []

    def groups_get(self, group: str) -> list:
        link = (stng.SCHEDULE_URL + stng.GROUP_EXISTS)
        return self._get(link, group)

    def teachers_get(self, teacher: str) -> list:
        link = (stng.SCHEDULE_URL + stng.TEACHER_EXISTS)
        return self._get(link, teacher)

    def get_schedule(self, group=None, sdate=None, edate=None, teacher=None) -> list:
        list_of_couple = self._get_page_with_schedule(group, sdate, edate, teacher)
        response = self._parse_schedule(list_of_couple, group, teacher)
        return response



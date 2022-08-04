from main import get_article_text, get_and_translate
from click.testing import CliRunner


def test_get_article_text():
    article_txt = get_article_text(
        "https://en.wikipedia.org/wiki/Artificial_intelligence_industry_in_China"
    )
    assert article_txt.__contains__(
        "rapidly developing multi-billion dollar industry"
    )
    assert len(article_txt) > 50


# def test_get_and_translate():
#     article_txt = get_article_text(
#         "https://en.wikipedia.org/wiki/Artificial_intelligence_industry_in_China"
#     )
#     translation = translate(article_txt)
#     assert '[INSERT TRANSLATION]' in translation

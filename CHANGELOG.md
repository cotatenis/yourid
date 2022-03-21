# Change Log
Arquivo para documentação das mudanças realizadas ao longo do projeto. O formato desse arquivo é baseado no [Keep a Changelog](http://keepachangelog.com/)
e o presente projeto adota o [Semantic Versioning](http://semver.org/).

## [0.5.0] - 2021-11-17
### [COT-402](https://ecoanalytics.atlassian.net/browse/COT-402)
### Adicionado
- Sobrescrito a função `image_downloaded` do objeto `ImagesPipeline` para garantir a persistência de apenas imagens que ainda não estão salvas no storage.

## [0.4.2] - 2021-11-13
### [COT-364](https://ecoanalytics.atlassian.net/browse/COT-364)
#### Alterado
- Alterado o regex da função `process_item` da classe `GCSPipeline`.

#### Removido
- Retirado o comentário dos pipelines do objeto `ITEM_PIPELINES`.
- Retirado o comentário dos pipelines do objeto `ITEM_PIPELINES`.

## [0.4.1] - 2021-11-01
### [COT-303](https://ecoanalytics.atlassian.net/browse/COT-303)
#### Adicionado
- Adicionado função `parse_sku` ao input_processor do field `sku` do objeto `YouridItem`.

## [0.4.0] - 2021-11-01
### [COT-303](https://ecoanalytics.atlassian.net/browse/COT-303)
#### Adicionado
- Adicionado spider `YourIdJordanSpider`.
- Adicionado spider `YourIdNikeSpider`.

#### Removido
- Removido a persistência de imagens na dimensão 800x600.

## [0.3.0] - 2021-10-15
### [COT-207](https://ecoanalytics.atlassian.net/browse/COT-207)
#### Alterado
- Adicionado a função `missing_price_field_message` no pipelines.

## [0.2.0] - 2021-10-09
### [COT-199](https://ecoanalytics.atlassian.net/browse/COT-199)
#### Alterado
- Alterado o parâmetro `IMAGES_THUMBS` para coletar imagens no padrão 400x400.


# DomashkaPy

## Для формирования отчёта необходимо:

1.  зайти в директорию с необходимыми тестами, к примеру: 
    ```
    cd 10_lesson
    ```

2.  После запустить команду для запуска теста и формирования отчёта(вместо "allure-result" можно придумать любое название папки)
    ```
    pytest --alluredir allure-result
    ```

3.  Сгенерировать отчёт для запуска(вместо "allure-result" можно придумать любое название папки)
    ```
    allure generate allure-result
    ```

4.  Запуск отчёта(вместо "allure-report" ваше название папки)
    ```
    allure open allure-report 
    ```

## Дополнительная информация

- `pytest` используется для запуска тестов.
- `allure` используется для генерации и открытия отчётов.

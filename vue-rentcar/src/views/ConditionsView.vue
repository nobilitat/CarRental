<template>
  <div class="container-md secondary">
    <div class="row mt-4">
      <h2>Условия предоставления автомобилей в аренду</h2>
      <h6>
        В отношении Заявителей, рассчитывающих взять на прокат транспортное
        средство на время своего пребывания на территории г. Хабаровска,
        предъявляются определенные требования, соответствие которым становится
        ключевым условием для получения и беспрепятственной эксплуатации ТС во
        время отпуска.
      </h6>
    </div>

    <div class="row">
        <b>Физ лица</b>
        <span>Для получения прокатного автотранспорта требуется:</span> <br>
        <!-- <b>1.</b> Российское гражданство<br>
        <b>2.</b> Подтверждения статуса гражданства<br>
        <b>3.</b> Постоянная прописка<br>
        <b>4.</b> Возраст от полных 23 лет (для аренды люксовых авто от 30 лет)<br>
        <b>5.</b> стаж вождения не менее 3 лет (для люксовых не менее 7 лет)</p> -->
        <span v-for="(condition, index) in conditionsList" :key="condition.id">
            <b>{{index+1}}. </b>{{condition.condition_name}} <br>
        </span> 
        <p></p>
    </div>

    <div class="row">
        <b>Юр лица</b>
        <p>Условия аренды авто для юридических лиц являются индивидуальными
            и устанавливаются рамками Договора между компанией и юрлицом
            по итогам предварительных договоренностей.
        </p>
    </div>

    <div class="row">
        <b>Получение</b>
        <p>Предоставленный в прокат транспорт бесплатно в течение времени
            передается Арендатору на стоянке вблизи офиса нашей компании.
            Одновременно с этим происходит передача сопроводительных
            бумаг. Заменой Путевого листа, который может потребоваться при
            остановке ТС с водителем-арендатором на стационарном посту
            ГИБДД, является прокатный Договор.
        </p>
        <p>Также осуществляется подача авто к:
            <ul>
                <li>аэропорту;</li>
                <li>ж/д вокзалу;</li>
                <li>произвольному адресу в пределах города Хабаровска.</li>
            </ul>
        </p>
    </div>

    <div class="row">
        <b>Возврат ТС</b>
        <p>Условия возврата авто являются общими для всех доступных классов
            и подлежат обязательному выполнению.
        </p>
        <p>Возвращаемая машина должна быть:
            <ul>
                <li>в технически исправном состоянии;</li>
                <li>без новых повреждений(сколов, царапин, потертостей, вмятин);</li>
                <li>чистой;</li>
                <li>с полным баком топлива.</li>
            </ul>
        </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      conditionsList: [],
    };
  },
  methods: {
    async getConditions() {
      const response = await fetch(
        `${this.$store.getters.getServerUrl}/cars/conditions/list`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      this.conditionsList = await response.json();
      console.log( this.conditionsList)
    },
  },
  created() {
      this.getConditions()
  },
};
</script>
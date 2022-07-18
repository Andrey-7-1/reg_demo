
// When checked, auto select RZD as company
function org_switch(checkbox)
{
    // Don't laugh I am new to JS!
    const short_name = "ОАО «РЖД»";
    const long_name = "Открытое Акционерное Общество «Российские Железные Дороги»";

    let elements = document.getElementsByClassName("org");
    for (let i = 0; i < elements.length; i++) {
        if (checkbox.checked) {
            document.getElementById("org-full").value = long_name;
            document.getElementById("org-short").value = short_name;
        }
        else elements[i].value = "";
        elements[i].disabled = checkbox.checked;
    }
}


function set_div_name_list() {
    let position_type = document.getElementById("division_name_type").value;
    let div_name_select = document.getElementById("division-name-select");
    let div_name_list = "dn_options-" + position_type.replace(' ', '_');
    if (document.getElementById(div_name_list) === null) {
        div_name_select.disabled = true;
        div_name_select.placeholder = "Заполните поле вверху";
    }
    else {
        div_name_select.setAttribute("list", div_name_list);
        div_name_select.disabled = false;
        div_name_select.placeholder = "Начните вводить название или выберите из перечня";
    }
}


function show_result( reference= {"normal": []}) {

    // convert reference from python dict to json
    reference = JSON.parse(JSON.stringify(reference));

    let result_1 = document.getElementById("position-type-select").value;

    let result_2 = document.getElementById("division-type-select").value;
    if (reference.normal.includes(result_2))
    {
        result_2 = reference.result[reference.normal.indexOf(result_2)];
    }

    let result_3 = document.getElementById("result-3").value;

    if (result_1.length + result_2.length + result_3.length > 0)
    {
        document.getElementById("position_result").innerHTML = result_1 + " " + result_2 + " " + result_3;
    }
}

function set_position_level(reference={'specialist': [], 'supervisor': []})
{
    // convert reference from python dict to json
    reference = JSON.parse(JSON.stringify(reference));

    let current_pos = document.getElementById("position-type-select").value;

    let select = document.getElementById("position_level");
    if (reference.specialist.includes(current_pos))
    {
        select.value = "Специалист";
        select.disabled = true;
    }
    else if (reference.supervisor.includes(current_pos))
    {
        select.value = "Руководитель";
        select.disabled = true;
    }
    else select.disabled = false;
}

function enable_fields_onsubmit()
{
    document.getElementById("org-short").disabled = false;
    document.getElementById("org-full").disabled = false;
    document.getElementById("position_level").disabled = false;
}
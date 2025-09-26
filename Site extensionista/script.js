function round1(v){return Math.round(v*10)/10}

function calcBMI(weight, height, units){
  if(units==='metric'){
    let m = height/100;
    return weight / (m*m);
  } else {
    const kg = weight * 0.45359237;
    const m = height * 0.0254;
    return kg / (m*m);
  }
}

function bmiCategory(bmi){
  if(bmi < 18.5) return {label:'Abaixo do peso', advice:'Procure orientação profissional.'};
  if(bmi < 25) return {label:'Peso normal', advice:'Mantenha hábitos saudáveis.'};
  if(bmi < 30) return {label:'Sobrepeso', advice:'Cuide da alimentação e faça exercícios.'};
  if(bmi < 35) return {label:'Obesidade (Grau I)', advice:'Consulte um profissional de saúde.'};
  if(bmi < 40) return {label:'Obesidade (Grau II)', advice:'Requer acompanhamento médico.'};
  return {label:'Obesidade grave (Grau III)', advice:'Avaliação médica urgente.'};
}

const form = document.getElementById('imcForm');
const unitsEl = document.getElementById('units');
const weightEl = document.getElementById('weight');
const heightEl = document.getElementById('height');
const bmiValueEl = document.getElementById('bmiValue');
const bmiCategoryEl = document.getElementById('bmiCategory');
const bmiAdviceEl = document.getElementById('bmiAdvice');

form.addEventListener('submit', function(e){
  e.preventDefault();
  const units = unitsEl.value;
  const w = parseFloat(weightEl.value);
  const h = parseFloat(heightEl.value);
  if(!w || !h){ alert('Preencha peso e altura corretamente.'); return; }
  const bmi = calcBMI(w,h,units);
  const bmiR = round1(bmi);
  const cat = bmiCategory(bmiR);
  bmiValueEl.textContent = bmiR + ' kg/m²';
  bmiCategoryEl.textContent = cat.label;
  bmiAdviceEl.textContent = cat.advice;
});

document.getElementById('clearBtn').addEventListener('click', function(){
  weightEl.value='';
  heightEl.value='';
  bmiValueEl.textContent='—';
  bmiCategoryEl.textContent='Nenhum cálculo ainda';
  bmiAdviceEl.textContent='';
});

document.getElementById('btnPrint').addEventListener('click', function(e){
  e.preventDefault();
  window.print();
});

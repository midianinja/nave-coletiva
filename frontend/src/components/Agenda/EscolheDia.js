import React from 'react';
import './escolheDia.scss';
import dropdown from '../../img/festivalninja-site-dropdown.svg';

const EscolheDia = () => {
  return (
    <div>
      <div className="selectday">
        <a>
          <label>Quinta-feira</label>
          <span>21.nov</span>
        </a>
        <img src={dropdown} alt="icone de seta apontando para baixo" />
      </div>
    </div>
  );
};

export default EscolheDia;

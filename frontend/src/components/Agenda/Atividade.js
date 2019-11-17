import React from 'react';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <div className="box">
            <h4>{atividade.titulo}</h4>
            <p>{atividade.inicio}</p>
            <p>{atividade.fim}</p>
          </div>
        </div>
    );
};

export default AtividadeComponent;

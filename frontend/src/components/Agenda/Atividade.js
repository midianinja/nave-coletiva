import React from 'react';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <h4>{atividade.titulo}</h4>
          <p>{atividade.inicio}</p>
        </div>
    );
};

export default AtividadeComponent;

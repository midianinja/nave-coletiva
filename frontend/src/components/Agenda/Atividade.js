import React from 'react';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <div className="box">
            <h4>{atividade.titulo}</h4>
          </div>
        </div>
    );
};

export default AtividadeComponent;

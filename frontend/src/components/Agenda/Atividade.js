import React from 'react';
import PropTypes from 'prop-types';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <div className="box">
            <h4>{atividade.titulo}</h4>
            <label>{`das ${atividade.inicio.slice(16,21)} às ${atividade.fim.slice(16, 21)}`}</label>
            {atividade.convidades.map((convidade, index) => (
              <h5 className="convidade" key={index}>{convidade.nome}</h5>))}
            <p>{atividade.descricao}</p>
          </div>
        </div>
    );
};

AtividadeComponent.propTypes = {
    atividade: PropTypes.object.isRequired,
};

export default AtividadeComponent;

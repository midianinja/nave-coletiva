import React from 'react';
import PropTypes from 'prop-types';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <div className="box">
            <h4>{atividade.titulo}</h4>
            <label>{`das ${atividade.inicio.slice(11, -4)} às ${atividade.fim.slice(11, -4)}`}</label>
          </div>
        </div>
    );
};

AtividadeComponent.propTypes = {
    atividade: PropTypes.object.isRequired,
};

export default AtividadeComponent;

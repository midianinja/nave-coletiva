import React from 'react';
import PropTypes from 'prop-types';

const AtividadeComponent = ({ atividade }) => {
    return (
        <div className="atividade">
          <div className="box">
            <h4>{atividade.titulo}</h4>
          </div>
        </div>
    );
};

AtividadeComponent.propTypes = {
    atividade: PropTypes.object.isRequired,
};

export default AtividadeComponent;

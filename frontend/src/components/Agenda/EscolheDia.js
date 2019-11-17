import React from 'react';
import PropTypes from 'prop-types';

import './escolheDia.scss';
import dropdown from '../../img/festivalninja-site-dropdown.svg';


class EscolheDia extends React.Component {
  state = {
    optionsVisible: false,
    label: 'Quinta-feira',
    span: '21.nov',
  }

  datas = [
    {
      label: 'Quinta-feira',
      span: '21.nov',
      data: '21/11',
    },
    {
      label: 'Sexta-feira',
      span: '22.nov',
      data: '22/11',
    },
    {
      label: 'Sábado',
      span: '23.nov',
      data: '23/11',
    },
    {
      label: 'Domingo',
      span: '24.nov',
      data: '24/11',
    },
  ]

  select({ data, label, span }) {
    this.props.onChange(data);
    this.setState({ optionsVisible: false, label, span });
  }

  render() {
    return (
      <div>
        <div className="selectday" onClick={() => this.setState({ optionsVisible: !this.state.optionsVisible })}>
          <a className="dia">
            <label>{this.state.label}</label>
            <span>{this.state.span}</span>
          </a>
          <a className="seta">
            <img src={dropdown} alt="icone de seta apontando para baixo" />
          </a>

          {this.state.optionsVisible &&
            <div className="options" >
              <div className="option-box">
                {this.datas.map((value, index) => (
                  <a className="dia" onClick={() => this.select(value)} key={index}>
                    <label>{value.label}</label>
                    <span>{value.span}</span>
                  </a>
                ))}
              </div>
            </div>}

        </div>
      </div>
    );
  }
}

EscolheDia.propTypes = {
  onChange: PropTypes.func.isRequired,
}

export default EscolheDia;

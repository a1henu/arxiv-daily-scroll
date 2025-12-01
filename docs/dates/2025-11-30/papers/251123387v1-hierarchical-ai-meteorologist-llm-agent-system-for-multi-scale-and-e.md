---
layout: default
title: Hierarchical AI-Meteorologist: LLM-Agent System for Multi-Scale and Explainable Weather Forecast Reporting
---

# Hierarchical AI-Meteorologist: LLM-Agent System for Multi-Scale and Explainable Weather Forecast Reporting
**arXiv**：[2511.23387v1](https://arxiv.org/abs/2511.23387) · [PDF](https://arxiv.org/pdf/2511.23387.pdf)  
**作者**：Daniil Sukhorukov, Andrei Zakharov, Nikita Glazkov, Katsiaryna Yanchanka, Vladimir Kirilin, Maxim Dubovitsky, Roman Sultimov, Yuri Maksimov, Ilya Makarov  

**一句话要点**：提出分层AI气象学家系统，通过多尺度推理和关键词生成实现可解释的天气预报报告。

**关键词**：分层推理, 可解释天气预报, LLM代理系统, 多尺度分析, 语义验证

## 3 点简述
- 核心问题：传统天气预报方法将预测视为平坦时间序列，缺乏对短期动态和长期趋势的捕捉。
- 方法要点：采用分层推理，结合小时、6小时和日聚合，将结构化气象输入转换为连贯叙述并提取关键词。
- 实验或效果：使用OpenWeather和Meteostat数据，验证分层上下文和关键词能提升LLM生成报告的可靠性和可解释性。

## 摘要（原文）

> We present the Hierarchical AI-Meteorologist, an LLM-agent system that generates explainable weather reports using a hierarchical forecast reasoning and weather keyword generation. Unlike standard approaches that treat forecasts as flat time series, our framework performs multi-scale reasoning across hourly, 6-hour, and daily aggregations to capture both short-term dynamics and long-term trends. Its core reasoning agent converts structured meteorological inputs into coherent narratives while simultaneously extracting a few keywords effectively summarizing the dominant meteorological events. These keywords serve as semantic anchors for validating consistency, temporal coherence and factual alignment of the generated reports. Using OpenWeather and Meteostat data, we demonstrate that hierarchical context and keyword-based validation substantially improve interpretability and robustness of LLM-generated weather narratives, offering a reproducible framework for semantic evaluation of automated meteorological reporting and advancing agent-based scientific reasoning.


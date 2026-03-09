---
layout: default
title: OD-RASE: Ontology-Driven Risk Assessment and Safety Enhancement for Autonomous Driving
---

# OD-RASE: Ontology-Driven Risk Assessment and Safety Enhancement for Autonomous Driving
**arXiv**：[2603.05936v1](https://arxiv.org/abs/2603.05936) · [PDF](https://arxiv.org/pdf/2603.05936.pdf)  
**作者**：Kota Shimomura, Masaki Nambata, Atsuya Ishikawa, Ryota Mimura, Takayuki Kawabuchi, Takayoshi Yamashita, Koki Inoue  

**一句话要点**：提出OD-RASE框架，通过本体驱动风险评估提升自动驾驶安全性

**关键词**：自动驾驶安全, 风险评估, 本体建模, 视觉语言模型, 基础设施改进, 数据集构建

## 3 点简述
- 自动驾驶系统在罕见或复杂道路场景中面临安全挑战，需主动风险缓解
- 基于道路交通系统知识构建本体，利用大视觉语言模型生成基础设施改进提案
- 实验显示本体驱动数据过滤能准确预测事故道路结构及改进计划

## 摘要（原文）

> Although autonomous driving systems demonstrate high perception performance, they still face limitations when handling rare situations or complex road structures. Such road infrastructures are designed for human drivers, safety improvements are typically introduced only after accidents occur. This reactive approach poses a significant challenge for autonomous systems, which require proactive risk mitigation. To address this issue, we propose OD-RASE, a framework for enhancing the safety of autonomous driving systems by detecting road structures that cause traffic accidents and connecting these findings to infrastructure development. First, we formalize an ontology based on specialized domain knowledge of road traffic systems. In parallel, we generate infrastructure improvement proposals using a large-scale visual language model (LVLM) and use ontology-driven data filtering to enhance their reliability. This process automatically annotates improvement proposals on pre-accident road images, leading to the construction of a new dataset. Furthermore, we introduce the Baseline approach (OD-RASE model), which leverages LVLM and a diffusion model to produce both infrastructure improvement proposals and generated images of the improved road environment. Our experiments demonstrate that ontology-driven data filtering enables highly accurate prediction of accident-causing road structures and the corresponding improvement plans. We believe that this work contributes to the overall safety of traffic environments and marks an important step toward the broader adoption of autonomous driving systems.


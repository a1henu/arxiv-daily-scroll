---
layout: default
title: PreScience: A Benchmark for Forecasting Scientific Contributions
---

# PreScience: A Benchmark for Forecasting Scientific Contributions
**arXiv**：[2602.20459v1](https://arxiv.org/abs/2602.20459) · [PDF](https://arxiv.org/pdf/2602.20459.pdf)  
**作者**：Anirudh Ajith, Amanpreet Singh, Jay DeYoung, Nadav Kunievsky, Austin C. Kozlowski, Oyvind Tafjord, James Evans, Daniel S. Weld, Tom Hope, Doug Downey  

**一句话要点**：提出PreScience基准以评估AI预测科学贡献的能力

**关键词**：科学预测基准, 贡献生成, LLM评估, 数据集构建, 任务分解, 影响预测

## 3 点简述
- 核心问题：AI能否基于历史科学记录预测未来科学进展
- 方法要点：将研究过程分解为四个生成任务，构建包含98K论文的数据集
- 实验或效果：前沿LLM在贡献生成任务中表现中等，合成语料多样性低于人类研究

## 摘要（原文）

> Can AI systems trained on the scientific record up to a fixed point in time forecast the scientific advances that follow? Such a capability could help researchers identify collaborators and impactful research directions, and anticipate which problems and methods will become central next. We introduce PreScience -- a scientific forecasting benchmark that decomposes the research process into four interdependent generative tasks: collaborator prediction, prior work selection, contribution generation, and impact prediction. PreScience is a carefully curated dataset of 98K recent AI-related research papers, featuring disambiguated author identities, temporally aligned scholarly metadata, and a structured graph of companion author publication histories and citations spanning 502K total papers. We develop baselines and evaluations for each task, including LACERScore, a novel LLM-based measure of contribution similarity that outperforms previous metrics and approximates inter-annotator agreement. We find substantial headroom remains in each task -- e.g. in contribution generation, frontier LLMs achieve only moderate similarity to the ground-truth (GPT-5, averages 5.6 on a 1-10 scale). When composed into a 12-month end-to-end simulation of scientific production, the resulting synthetic corpus is systematically less diverse and less novel than human-authored research from the same period.


---
layout: default
title: Explaining Synergistic Effects in Social Recommendations
---

# Explaining Synergistic Effects in Social Recommendations
**arXiv**：[2601.18151v1](https://arxiv.org/abs/2601.18151) · [PDF](https://arxiv.org/pdf/2601.18151.pdf)  
**作者**：Yicong Li, Shan Jin, Qi Liu, Shuo Wang, Jiaying Liu, Shuo Yu, Qiang Zhang, Kuanjiu Zhou, Feng Xia  

**一句话要点**：提出SemExplainer以解释社交推荐中的协同效应，通过识别子图增强可解释性。

**关键词**：社交推荐, 协同效应解释, 图信息增益, 子图识别, 可解释性增强

## 3 点简述
- 核心问题：社交推荐中多网络协同效应的非线性与不透明性降低可解释性，现有方法无法解释协同效应。
- 方法要点：基于图信息增益量化协同效应，提取子图并优化条件熵以识别协同子图，生成推荐解释路径。
- 实验或效果：在三个数据集上验证SemExplainer优于基线方法，提供更优的协同效应解释。

## 摘要（原文）

> In social recommenders, the inherent nonlinearity and opacity of synergistic effects across multiple social networks hinders users from understanding how diverse information is leveraged for recommendations, consequently diminishing explainability. However, existing explainers can only identify the topological information in social networks that significantly influences recommendations, failing to further explain the synergistic effects among this information. Inspired by existing findings that synergistic effects enhance mutual information between inputs and predictions to generate information gain, we extend this discovery to graph data. We quantify graph information gain to identify subgraphs embodying synergistic effects. Based on the theoretical insights, we propose SemExplainer, which explains synergistic effects by identifying subgraphs that embody them. SemExplainer first extracts explanatory subgraphs from multi-view social networks to generate preliminary importance explanations for recommendations. A conditional entropy optimization strategy to maximize information gain is developed, thereby further identifying subgraphs that embody synergistic effects from explanatory subgraphs. Finally, SemExplainer searches for paths from users to recommended items within the synergistic subgraphs to generate explanations for the recommendations. Extensive experiments on three datasets demonstrate the superiority of SemExplainer over baseline methods, providing superior explanations of synergistic effects.


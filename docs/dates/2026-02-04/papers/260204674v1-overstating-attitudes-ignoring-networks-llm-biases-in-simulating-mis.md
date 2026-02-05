---
layout: default
title: Overstating Attitudes, Ignoring Networks: LLM Biases in Simulating Misinformation Susceptibility
---

# Overstating Attitudes, Ignoring Networks: LLM Biases in Simulating Misinformation Susceptibility
**arXiv**：[2602.04674v1](https://arxiv.org/abs/2602.04674) · [PDF](https://arxiv.org/pdf/2602.04674.pdf)  
**作者**：Eun Cheol Choi, Lindsay E. Young, Emilio Ferrara  

**一句话要点**：揭示LLM在模拟虚假信息易感性中的偏见，强调其更适用于诊断而非替代人类判断

**关键词**：大型语言模型偏见, 虚假信息易感性模拟, 计算社会科学, 调查响应生成, 网络特征忽略, 态度特征高估

## 3 点简述
- 核心问题：LLM作为人类判断代理在计算社会科学中的有效性，尤其在虚假信息易感性模式再现方面存在不确定性
- 方法要点：基于社会调查数据构建参与者档案，测试LLM模拟受访者是否能复制人类对虚假信息的信念和分享模式
- 实验或效果：LLM输出与人类响应分布有适度相关，但高估信念与分享关联，且线性模型过度强调态度特征而忽略网络特征

## 摘要（原文）

> Large language models (LLMs) are increasingly used as proxies for human judgment in computational social science, yet their ability to reproduce patterns of susceptibility to misinformation remains unclear. We test whether LLM-simulated survey respondents, prompted with participant profiles drawn from social survey data measuring network, demographic, attitudinal and behavioral features, can reproduce human patterns of misinformation belief and sharing. Using three online surveys as baselines, we evaluate whether LLM outputs match observed response distributions and recover feature-outcome associations present in the original survey data. LLM-generated responses capture broad distributional tendencies and show modest correlation with human responses, but consistently overstate the association between belief and sharing. Linear models fit to simulated responses exhibit substantially higher explained variance and place disproportionate weight on attitudinal and behavioral features, while largely ignoring personal network characteristics, relative to models fit to human responses. Analyses of model-generated reasoning and LLM training data suggest that these distortions reflect systematic biases in how misinformation-related concepts are represented. Our findings suggest that LLM-based survey simulations are better suited for diagnosing systematic divergences from human judgment than for substituting it.


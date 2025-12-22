---
layout: default
title: ScoutGPT: Capturing Player Impact from Team Action Sequences Using GPT-Based Framework
---

# ScoutGPT: Capturing Player Impact from Team Action Sequences Using GPT-Based Framework
**arXiv**：[2512.17266v1](https://arxiv.org/abs/2512.17266) · [PDF](https://arxiv.org/pdf/2512.17266.pdf)  
**作者**：Miru Hong, Minho Lee, Geonhee Jo, Jae-Hee So, Pascal Bauer, Sang-Ki Ko  

**一句话要点**：提出EventGPT，基于GPT框架预测足球事件以评估球员转会适应性

**关键词**：事件序列预测, 球员价值评估, 反事实模拟, 足球分析, GPT框架

## 3 点简述
- 问题：现有方法依赖静态统计，难以捕捉球员在新战术环境中的动态贡献
- 方法：使用GPT风格自回归变换器，基于球员身份和上下文预测事件类型、位置、时间及残差价值
- 实验：在英超数据上优于基线，并通过反事实模拟展示转会分析实用性

## 摘要（原文）

> Transfers play a pivotal role in shaping a football club's success, yet forecasting whether a transfer will succeed remains difficult due to the strong context-dependence of on-field performance. Existing evaluation practices often rely on static summary statistics or post-hoc value models, which fail to capture how a player's contribution adapts to a new tactical environment or different teammates. To address this gap, we introduce EventGPT, a player-conditioned, value-aware next-event prediction model built on a GPT-style autoregressive transformer. Our model treats match play as a sequence of discrete tokens, jointly learning to predict the next on-ball action's type, location, timing, and its estimated residual On-Ball Value (rOBV) based on the preceding context and player identity. A key contribution of this framework is the ability to perform counterfactual simulations. By substituting learned player embeddings into new event sequences, we can simulate how a player's behavioral distribution and value profile would change when placed in a different team or tactical structure. Evaluated on five seasons of Premier League event data, EventGPT outperforms existing sequence-based baselines in next-event prediction accuracy and spatial precision. Furthermore, we demonstrate the model's practical utility for transfer analysis through case studies-such as comparing striker performance across different systems and identifying stylistic replacements for specific roles-showing that our approach provides a principled method for evaluating transfer fit.


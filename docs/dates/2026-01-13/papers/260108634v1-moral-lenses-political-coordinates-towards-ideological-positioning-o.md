---
layout: default
title: Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs
---

# Moral Lenses, Political Coordinates: Towards Ideological Positioning of Morally Conditioned LLMs
**arXiv**：[2601.08634v1](https://arxiv.org/abs/2601.08634) · [PDF](https://arxiv.org/pdf/2601.08634.pdf)  
**作者**：Chenchen Yuan, Bolei Ma, Zheyu Zhang, Bardh Prenkaj, Frauke Kreuter, Gjergji Kasneci  

**一句话要点**：提出道德条件化方法以探究大语言模型中道德价值与政治立场的因果关系

**关键词**：大语言模型对齐, 道德价值条件化, 政治立场评估, 社会心理学, 可控生成

## 3 点简述
- 核心问题：现有评估主要依赖直接探测或人口统计角色工程来揭示大语言模型的政治偏见，但政治意识形态在心理学中也被视为基本道德直觉的下游后果。
- 方法要点：通过将道德取向作为可控条件，让模型支持或拒绝特定道德价值，并使用政治罗盘测试评估其政治立场的偏移。
- 实验或效果：发现道德条件化能诱导模型在政治坐标上产生显著、价值特定的偏移，且这些效应受角色框架和模型规模的系统调节，在不同评估工具中稳健。

## 摘要（原文）

> While recent research has systematically documented political orientation in large language models (LLMs), existing evaluations rely primarily on direct probing or demographic persona engineering to surface ideological biases. In social psychology, however, political ideology is also understood as a downstream consequence of fundamental moral intuitions. In this work, we investigate the causal relationship between moral values and political positioning by treating moral orientation as a controllable condition. Rather than simply assigning a demographic persona, we condition models to endorse or reject specific moral values and evaluate the resulting shifts on their political orientations, using the Political Compass Test. By treating moral values as lenses, we observe how moral conditioning actively steers model trajectories across economic and social dimensions. Our findings show that such conditioning induces pronounced, value-specific shifts in models' political coordinates. We further notice that these effects are systematically modulated by role framing and model scale, and are robust across alternative assessment instruments instantiating the same moral value. This highlights that effective alignment requires anchoring political assessments within the context of broader social values including morality, paving the way for more socially grounded alignment techniques.


---
layout: default
title: Do Sparse Autoencoders Identify Reasoning Features in Language Models?
---

# Do Sparse Autoencoders Identify Reasoning Features in Language Models?
**arXiv**：[2601.05679v1](https://arxiv.org/abs/2601.05679) · [PDF](https://arxiv.org/pdf/2601.05679.pdf)  
**作者**：George Ma, Zhongyuan Liang, Irene Y. Chen, Somayeh Sojoudi  

**一句话要点**：提出基于因果干预与LLM引导的证伪框架，揭示稀疏自编码器在语言模型中捕获的推理特征主要依赖语言相关性而非计算过程。

**关键词**：稀疏自编码器, 推理特征, 因果干预, 语言模型分析, 特征证伪

## 3 点简述
- 核心问题：探究稀疏自编码器是否识别语言模型中的真实推理特征，而非表面语言关联。
- 方法要点：结合因果令牌注入实验和LLM引导证伪，测试特征激活是否反映推理过程。
- 实验或效果：在20种配置下，多数特征对令牌干预敏感，未发现满足真实推理标准的特征，性能影响有限。

## 摘要（原文）

> We investigate whether sparse autoencoders (SAEs) identify genuine reasoning features in large language models (LLMs). Starting from features selected using standard contrastive activation methods, we introduce a falsification-oriented framework that combines causal token injection experiments and LLM-guided falsification to test whether feature activation reflects reasoning processes or superficial linguistic correlates. Across 20 configurations spanning multiple model families, layers, and reasoning datasets, we find that identified reasoning features are highly sensitive to token-level interventions. Injecting a small number of feature-associated tokens into non-reasoning text is sufficient to elicit strong activation for 59% to 94% of features, indicating reliance on lexical artifacts. For the remaining features that are not explained by simple token triggers, LLM-guided falsification consistently produces non-reasoning inputs that activate the feature and reasoning inputs that do not, with no analyzed feature satisfying our criteria for genuine reasoning behavior. Steering these features yields minimal changes or slight degradations in benchmark performance. Together, these results suggest that SAE features identified by contrastive approaches primarily capture linguistic correlates of reasoning rather than the underlying reasoning computations themselves.


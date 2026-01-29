---
layout: default
title: Context Tokens are Anchors: Understanding the Repetition Curse in dMLLMs from an Information Flow Perspective
---

# Context Tokens are Anchors: Understanding the Repetition Curse in dMLLMs from an Information Flow Perspective
**arXiv**：[2601.20520v1](https://arxiv.org/abs/2601.20520) · [PDF](https://arxiv.org/pdf/2601.20520.pdf)  
**作者**：Qiyan Zhao, Xiaofeng Zhang, Shuochen Chang, Qianyu Chen, Xiaosong Yuan, Xuhang Chen, Luoqi Liu, Jiajun Zhang, Xu-Yao Zhang, Da-Han Wang  

**一句话要点**：提出CoTA方法以解决扩散多模态大语言模型中的重复生成问题

**关键词**：扩散多模态大语言模型, 重复生成, 信息流分析, 上下文令牌, 解码加速, 注意力机制

## 3 点简述
- 分析重复生成的信息流机制，发现上下文令牌作为锚点引导预测
- 提出CoTA方法，增强上下文令牌注意力并引入解码惩罚项
- 实验显示CoTA有效缓解重复，提升通用任务性能

## 摘要（原文）

> Recent diffusion-based Multimodal Large Language Models (dMLLMs) suffer from high inference latency and therefore rely on caching techniques to accelerate decoding. However, the application of cache mechanisms often introduces undesirable repetitive text generation, a phenomenon we term the \textbf{Repeat Curse}. To better investigate underlying mechanism behind this issue, we analyze repetition generation through the lens of information flow. Our work reveals three key findings: (1) context tokens aggregate semantic information as anchors and guide the final predictions; (2) as information propagates across layers, the entropy of context tokens converges in deeper layers, reflecting the model's growing prediction certainty; (3) Repetition is typically linked to disruptions in the information flow of context tokens and to the inability of their entropy to converge in deeper layers. Based on these insights, we present \textbf{CoTA}, a plug-and-play method for mitigating repetition. CoTA enhances the attention of context tokens to preserve intrinsic information flow patterns, while introducing a penalty term to the confidence score during decoding to avoid outputs driven by uncertain context tokens. With extensive experiments, CoTA demonstrates significant effectiveness in alleviating repetition and achieves consistent performance improvements on general tasks. Code is available at https://github.com/ErikZ719/CoTA


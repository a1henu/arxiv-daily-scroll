---
layout: default
title: MetaOthello: A Controlled Study of Multiple World Models in Transformers
---

# MetaOthello: A Controlled Study of Multiple World Models in Transformers
**arXiv**：[2602.23164v1](https://arxiv.org/abs/2602.23164) · [PDF](https://arxiv.org/pdf/2602.23164.pdf)  
**作者**：Aviral Chawla, Galen Hall, Juniper Lovato  

**一句话要点**：提出MetaOthello以研究Transformer中多个世界模型的共享表示组织

**关键词**：世界模型, Transformer表示学习, 机制可解释性, Othello变体, 线性探针, 共享表示

## 3 点简述
- 核心问题：Transformer如何组织多个潜在冲突的世界模型，而非孤立研究单一能力
- 方法要点：设计Othello变体套件，训练小GPT于混合数据，分析共享表示空间
- 实验或效果：发现共享棋盘状态表示，线性探针可跨变体干预，层间表示随规则重叠而分化

## 摘要（原文）

> Foundation models must handle multiple generative processes, yet mechanistic interpretability largely studies capabilities in isolation; it remains unclear how a single transformer organizes multiple, potentially conflicting "world models". Previous experiments on Othello playing neural-networks test world-model learning but focus on a single game with a single set of rules. We introduce MetaOthello, a controlled suite of Othello variants with shared syntax but different rules or tokenizations, and train small GPTs on mixed-variant data to study how multiple world models are organized in a shared representation space. We find that transformers trained on mixed-game data do not partition their capacity into isolated sub-models; instead, they converge on a mostly shared board-state representation that transfers causally across variants. Linear probes trained on one variant can intervene on another's internal state with effectiveness approaching that of matched probes. For isomorphic games with token remapping, representations are equivalent up to a single orthogonal rotation that generalizes across layers. When rules partially overlap, early layers maintain game-agnostic representations while a middle layer identifies game identity, and later layers specialize. MetaOthello offers a path toward understanding not just whether transformers learn world models, but how they organize many at once.


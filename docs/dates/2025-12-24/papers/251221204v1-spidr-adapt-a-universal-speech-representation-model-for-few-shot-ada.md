---
layout: default
title: SpidR-Adapt: A Universal Speech Representation Model for Few-Shot Adaptation
---

# SpidR-Adapt: A Universal Speech Representation Model for Few-Shot Adaptation
**arXiv**：[2512.21204v1](https://arxiv.org/abs/2512.21204) · [PDF](https://arxiv.org/pdf/2512.21204.pdf)  
**作者**：Mahi Luthra, Jiayi Shen, Maxime Poli, Angelo Ortiz, Yosuke Higuchi, Youssef Benchekroun, Martin Gleize, Charles-Eric Saint-James, Dongyan Lin, Phillip Rust, Angel Villar, Surya Parimi, Vanessa Stark, Rashel Moritz, Juan Pino, Yann LeCun, Emmanuel Dupoux  

**一句话要点**：提出SpidR-Adapt，通过元学习框架实现少样本语音表示适应，提升数据效率。

**关键词**：语音表示学习, 元学习, 少样本适应, 双层优化, 数据效率, 自监督学习

## 3 点简述
- 核心问题：自监督语音模型数据需求高，与人类婴儿高效学习形成差距。
- 方法要点：采用多任务自适应预训练协议和一阶双层优化，降低计算成本。
- 实验或效果：在少于1小时目标语言音频上训练，超越领域内模型，数据效率提升100倍以上。

## 摘要（原文）

> Human infants, with only a few hundred hours of speech exposure, acquire basic units of new languages, highlighting a striking efficiency gap compared to the data-hungry self-supervised speech models. To address this gap, this paper introduces SpidR-Adapt for rapid adaptation to new languages using minimal unlabeled data. We cast such low-resource speech representation learning as a meta-learning problem and construct a multi-task adaptive pre-training (MAdaPT) protocol which formulates the adaptation process as a bi-level optimization framework. To enable scalable meta-training under this framework, we propose a novel heuristic solution, first-order bi-level optimization (FOBLO), avoiding heavy computation costs. Finally, we stabilize meta-training by using a robust initialization through interleaved supervision which alternates self-supervised and supervised objectives. Empirically, SpidR-Adapt achieves rapid gains in phonemic discriminability (ABX) and spoken language modeling (sWUGGY, sBLIMP, tSC), improving over in-domain language models after training on less than 1h of target-language audio, over $100\times$ more data-efficient than standard training. These findings highlight a practical, architecture-agnostic path toward biologically inspired, data-efficient representations. We open-source the training code and model checkpoints at https://github.com/facebookresearch/spidr-adapt.


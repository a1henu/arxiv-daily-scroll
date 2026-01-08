---
layout: default
title: EASLT: Emotion-Aware Sign Language Translation
---

# EASLT: Emotion-Aware Sign Language Translation
**arXiv**：[2601.03549v1](https://arxiv.org/abs/2601.03549) · [PDF](https://arxiv.org/pdf/2601.03549.pdf)  
**作者**：Guobin Tu, Di Weng  

**一句话要点**：提出EASLT框架，通过情感感知融合解决手语翻译中面部表情语义模糊问题。

**关键词**：手语翻译, 情感感知, 多模态融合, 无注释方法, 语义消歧

## 3 点简述
- 核心问题：无注释手语翻译方法常忽略面部表情语义，导致相同手势产生歧义。
- 方法要点：引入情感编码器捕获连续情感动态，并通过情感感知融合模块自适应调整时空特征。
- 实验或效果：在PHOENIX14T和CSL-Daily基准上取得先进性能，消融研究证实情感建模提升翻译保真度。

## 摘要（原文）

> Sign Language Translation (SLT) is a complex cross-modal task requiring the integration of Manual Signals (MS) and Non-Manual Signals (NMS). While recent gloss-free SLT methods have made strides in translating manual gestures, they frequently overlook the semantic criticality of facial expressions, resulting in ambiguity when distinct concepts share identical manual articulations. To address this, we present **EASLT** (**E**motion-**A**ware **S**ign **L**anguage **T**ranslation), a framework that treats facial affect not as auxiliary information, but as a robust semantic anchor. Unlike methods that relegate facial expressions to a secondary role, EASLT incorporates a dedicated emotional encoder to capture continuous affective dynamics. These representations are integrated via a novel *Emotion-Aware Fusion* (EAF) module, which adaptively recalibrates spatio-temporal sign features based on affective context to resolve semantic ambiguities. Extensive evaluations on the PHOENIX14T and CSL-Daily benchmarks demonstrate that EASLT establishes advanced performance among gloss-free methods, achieving BLEU-4 scores of 26.15 and 22.80, and BLEURT scores of 61.0 and 57.8, respectively. Ablation studies confirm that explicitly modeling emotion effectively decouples affective semantics from manual dynamics, significantly enhancing translation fidelity. Code is available at https://github.com/TuGuobin/EASLT.


---
layout: default
title: Mitigating Legibility Tax with Decoupled Prover-Verifier Games
---

# Mitigating Legibility Tax with Decoupled Prover-Verifier Games
**arXiv**：[2602.23248v1](https://arxiv.org/abs/2602.23248) · [PDF](https://arxiv.org/pdf/2602.23248.pdf)  
**作者**：Yegon Kim, Juho Lee  

**一句话要点**：提出解耦证明者-验证者游戏以缓解大型语言模型输出可检查性中的可读性税问题

**关键词**：大型语言模型, 可检查性, 证明者-验证者游戏, 可读性税, 翻译器模型, 解耦训练

## 3 点简述
- 核心问题：大型语言模型输出可检查性提升时，准确性下降，称为可读性税
- 方法要点：通过解耦正确性与可检查性条件，训练翻译器模型将固定求解器输出转换为可检查形式
- 实验或效果：未知，但方法旨在保留求解器答案的同时实现可检查性

## 摘要（原文）

> As large language models become increasingly capable, it is critical that their outputs can be easily checked by less capable systems. Prover-verifier games can be used to improve checkability of model outputs, but display a degradation in accuracy compared to a baseline trained only to maximize correctness -- a phenonemon named legibility tax. We propose a solution by decoupling the correctness from the checkability condition and instead training a "translator" model that turns a fixed solver model's solution into a checkable form. This allows us to first train the solver to maximize correctness, and then train the translator to translate the solver into a checkable form while retaining the solver's answer. To accommodate this new objective of translation, we formulate a decoupled prover-verifier game where the equilibria correspond to faithful and checkable translators.


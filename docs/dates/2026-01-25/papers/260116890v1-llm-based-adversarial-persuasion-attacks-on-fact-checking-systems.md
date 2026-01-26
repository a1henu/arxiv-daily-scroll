---
layout: default
title: LLM-Based Adversarial Persuasion Attacks on Fact-Checking Systems
---

# LLM-Based Adversarial Persuasion Attacks on Fact-Checking Systems
**arXiv**：[2601.16890v1](https://arxiv.org/abs/2601.16890) · [PDF](https://arxiv.org/pdf/2601.16890.pdf)  
**作者**：João A. Leite, Olesya Razuvayevskaya, Kalina Bontcheva, Carolina Scarton  

**一句话要点**：提出基于LLM的劝说式对抗攻击，以降低自动事实核查系统的性能。

**关键词**：自动事实核查, 对抗攻击, 劝说技术, 大语言模型, 证据检索

## 3 点简述
- 核心问题：自动事实核查系统易受对抗攻击，现有方法未利用劝说技术。
- 方法要点：使用生成式LLM重述声明，应用15种劝说技术，分6类进行攻击。
- 实验或效果：在FEVER和FEVEROUS基准上，攻击显著降低验证和证据检索性能。

## 摘要（原文）

> Automated fact-checking (AFC) systems are susceptible to adversarial attacks, enabling false claims to evade detection. Existing adversarial frameworks typically rely on injecting noise or altering semantics, yet no existing framework exploits the adversarial potential of persuasion techniques, which are widely used in disinformation campaigns to manipulate audiences. In this paper, we introduce a novel class of persuasive adversarial attacks on AFCs by employing a generative LLM to rephrase claims using persuasion techniques. Considering 15 techniques grouped into 6 categories, we study the effects of persuasion on both claim verification and evidence retrieval using a decoupled evaluation strategy. Experiments on the FEVER and FEVEROUS benchmarks show that persuasion attacks can substantially degrade both verification performance and evidence retrieval. Our analysis identifies persuasion techniques as a potent class of adversarial attacks, highlighting the need for more robust AFC systems.


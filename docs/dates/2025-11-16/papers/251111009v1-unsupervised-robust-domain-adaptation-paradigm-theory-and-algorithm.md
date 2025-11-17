---
layout: default
title: Unsupervised Robust Domain Adaptation: Paradigm, Theory and Algorithm
---

# Unsupervised Robust Domain Adaptation: Paradigm, Theory and Algorithm
**arXiv**：[2511.11009v1](https://arxiv.org/abs/2511.11009) · [PDF](https://arxiv.org/pdf/2511.11009.pdf)  
**作者**：Fuxiang Huang, Xiaowei Fu, Shiyu Ye, Lina Ma, Wen Li, Xinbo Gao, David Zhang, Lei Zhang  

**一句话要点**：提出无监督鲁棒域适应范式与DART算法，以解决域适应中对抗攻击鲁棒性问题。

**关键词**：无监督域适应, 对抗鲁棒性, 泛化理论, 解耦蒸馏, DART算法

## 3 点简述
- 核心问题：传统对抗训练在无监督域适应中失效，因存在内在纠缠挑战。
- 方法要点：引入URDA范式与DART算法，通过解耦蒸馏实现鲁棒化训练。
- 实验或效果：在多个数据集上验证，DART增强鲁棒性同时保持域适应能力。

## 摘要（原文）

> Unsupervised domain adaptation (UDA) aims to transfer knowledge from a label-rich source domain to an unlabeled target domain by addressing domain shifts. Most UDA approaches emphasize transfer ability, but often overlook robustness against adversarial attacks. Although vanilla adversarial training (VAT) improves the robustness of deep neural networks, it has little effect on UDA. This paper focuses on answering three key questions: 1) Why does VAT, known for its defensive effectiveness, fail in the UDA paradigm? 2) What is the generalization bound theory under attacks and how does it evolve from classical UDA theory? 3) How can we implement a robustification training procedure without complex modifications? Specifically, we explore and reveal the inherent entanglement challenge in general UDA+VAT paradigm, and propose an unsupervised robust domain adaptation (URDA) paradigm. We further derive the generalization bound theory of the URDA paradigm so that it can resist adversarial noise and domain shift. To the best of our knowledge, this is the first time to establish the URDA paradigm and theory. We further introduce a simple, novel yet effective URDA algorithm called Disentangled Adversarial Robustness Training (DART), a two-step training procedure that ensures both transferability and robustness. DART first pre-trains an arbitrary UDA model, and then applies an instantaneous robustification post-training step via disentangled distillation.Experiments on four benchmark datasets with/without attacks show that DART effectively enhances robustness while maintaining domain adaptability, and validate the URDA paradigm and theory.


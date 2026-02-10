---
layout: default
title: Linearization Explains Fine-Tuning in Large Language Models
---

# Linearization Explains Fine-Tuning in Large Language Models
**arXiv**：[2602.08239v1](https://arxiv.org/abs/2602.08239) · [PDF](https://arxiv.org/pdf/2602.08239.pdf)  
**作者**：Zahra Rahimi Afzal, Tara Esmaeilbeig, Mojtaba Soltanalian, Mesrob I. Ohannessian  

**一句话要点**：通过线性化解释大语言模型微调机制，揭示神经正切核与性能关联

**关键词**：参数高效微调, 神经正切核, 线性化分析, 大语言模型, 低秩适应

## 3 点简述
- 研究参数高效微调（PEFT）机制，聚焦训练动态与泛化性能
- 引入欧氏距离归纳偏置，将微调动态等价于神经正切核（NTK）学习
- 实证验证理论于LoRA，分析NTK谱与微调性能的强相关性

## 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) is a popular class of techniques that strive to adapt large models in a scalable and resource-efficient manner. Yet, the mechanisms underlying their training performance and generalization remain underexplored. In this paper, we provide several insights into such fine-tuning through the lens of linearization. Fine-tuned models are often implicitly encouraged to remain close to the pretrained model. By making this explicit, using an Euclidean distance inductive bias in parameter space, we show that fine-tuning dynamics become equivalent to learning with the positive-definite neural tangent kernel (NTK). We specifically analyze how close the fully linear and the linearized fine-tuning optimizations are, based on the strength of the regularization. This allows us to be pragmatic about how good a model linearization is when fine-tuning large language models (LLMs). When linearization is a good model, our findings reveal a strong correlation between the eigenvalue spectrum of the NTK and the performance of model adaptation. Motivated by this, we give spectral perturbation bounds on the NTK induced by the choice of layers selected for fine-tuning. We empirically validate our theory on Low Rank Adaptation (LoRA) on LLMs. These insights not only characterize fine-tuning but also have the potential to enhance PEFT techniques, paving the way to better informed and more nimble adaptation in LLMs.


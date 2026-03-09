---
layout: default
title: COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics
---

# COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics
**arXiv**：[2603.06495v1](https://arxiv.org/abs/2603.06495) · [PDF](https://arxiv.org/pdf/2603.06495.pdf)  
**作者**：Kartik Sharma, Rakshit S. Trivedi  

**一句话要点**：提出COLD-Steer框架，通过近似梯度下降动态实现少样本激活引导以控制大语言模型行为。

**关键词**：激活引导, 大语言模型控制, 推理时优化, 少样本学习, 梯度近似, 多元对齐

## 3 点简述
- 当前激活引导方法存在样本效率与信号提取的权衡问题，需大量示例或效果不佳。
- COLD-Steer基于核近似和有限差分法，在推理时模拟微调效果，无需参数更新。
- 实验显示，在多种任务中，COLD-Steer用50倍少样本达到95%引导效果，支持多元对齐。

## 摘要（原文）

> Activation steering methods enable inference-time control of large language model (LLM) behavior without retraining, but current approaches face a fundamental trade-off: sample-efficient methods suboptimally capture steering signals from labeled examples, while methods that better extract these signals require hundreds to thousands of examples. We introduce COLD-Steer, a training-free framework that steers LLM activations by approximating the representational changes that would result from gradient descent on in-context examples. Our key insight is that the effect of fine-tuning on a small set of examples can be efficiently approximated at inference time without actual parameter updates. We formalize this through two complementary approaches: (i) a unit kernel approximation method that updates the activations directly using gradients with respect to them, normalized across examples, and (ii) a finite-difference approximation requiring only two forward passes regardless of example count. Experiments across a variety of steering tasks and benchmarks demonstrate that COLD-Steer achieves upto 95% steering effectiveness while using 50 times fewer samples compared to the best baseline. COLD-Steer facilitates accommodating diverse perspectives without extensive demonstration data, which we validate through our experiments on pluralistic alignment tasks. Our framework opens new possibilities for adaptive, context-aware model control that can flexibly address varying loss-driven human preferences through principled approximation of learning dynamics rather than specialized training procedures.


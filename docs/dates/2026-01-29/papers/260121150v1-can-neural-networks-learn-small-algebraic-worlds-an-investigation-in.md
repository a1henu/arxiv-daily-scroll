---
layout: default
title: Can Neural Networks Learn Small Algebraic Worlds? An Investigation Into the Group-theoretic Structures Learned By Narrow Models Trained To Predict Group Operations
---

# Can Neural Networks Learn Small Algebraic Worlds? An Investigation Into the Group-theoretic Structures Learned By Narrow Models Trained To Predict Group Operations
**arXiv**：[2601.21150v1](https://arxiv.org/abs/2601.21150) · [PDF](https://arxiv.org/pdf/2601.21150.pdf)  
**作者**：Henry Kvinge, Andrew Aguilar, Nayda Farnsworth, Grace O'Brien, Robert Jasper, Sarah Scullen, Helen Jenne  

**一句话要点**：探究窄模型在预测群运算任务中学习群论结构的能力

**关键词**：神经网络, 群论学习, 数学结构提取, 表示学习, 代数性质

## 3 点简述
- 核心问题：窄模型能否从固定数学任务中学习更广泛的数学结构，超越简单问答。
- 方法要点：训练神经网络预测群运算，设计测试套件评估模型对群论概念如单位元、交换性的捕获。
- 实验或效果：模型能捕获交换性等抽象性质，但无法提取单位元概念，表明表示可蒸馏有趣结构。

## 摘要（原文）

> While a real-world research program in mathematics may be guided by a motivating question, the process of mathematical discovery is typically open-ended. Ideally, exploration needed to answer the original question will reveal new structures, patterns, and insights that are valuable in their own right. This contrasts with the exam-style paradigm in which the machine learning community typically applies AI to math. To maximize progress in mathematics using AI, we will need to go beyond simple question answering. With this in mind, we explore the extent to which narrow models trained to solve a fixed mathematical task learn broader mathematical structure that can be extracted by a researcher or other AI system. As a basic test case for this, we use the task of training a neural network to predict a group operation (for example, performing modular arithmetic or composition of permutations). We describe a suite of tests designed to assess whether the model captures significant group-theoretic notions such as the identity element, commutativity, or subgroups. Through extensive experimentation we find evidence that models learn representations capable of capturing abstract algebraic properties. For example, we find hints that models capture the commutativity of modular arithmetic. We are also able to train linear classifiers that reliably distinguish between elements of certain subgroups (even though no labels for these subgroups are included in the data). On the other hand, we are unable to extract notions such as the concept of the identity element. Together, our results suggest that in some cases the representations of even small neural networks can be used to distill interesting abstract structure from new mathematical objects.


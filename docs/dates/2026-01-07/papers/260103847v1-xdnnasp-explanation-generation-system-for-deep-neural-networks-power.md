---
layout: default
title: xDNN(ASP): Explanation Generation System for Deep Neural Networks powered by Answer Set Programming
---

# xDNN(ASP): Explanation Generation System for Deep Neural Networks powered by Answer Set Programming
**arXiv**：[2601.03847v1](https://arxiv.org/abs/2601.03847) · [PDF](https://arxiv.org/pdf/2601.03847.pdf)  
**作者**：Ly Ly Trieu, Tran Cao Son  

**一句话要点**：提出xDNN(ASP)系统，基于答案集编程为深度神经网络生成全局解释

**关键词**：可解释人工智能, 深度神经网络, 答案集编程, 全局解释, 逻辑程序提取

## 3 点简述
- 核心问题：现有解释方法忽视网络结构，难以提供全局解释
- 方法要点：从训练数据和模型中提取答案集语义的逻辑程序，模拟网络行为
- 实验或效果：在合成数据集上验证程序预测准确性，并揭示特征重要性和隐藏节点影响

## 摘要（原文）

> Explainable artificial intelligence (xAI) has gained significant attention in recent years. Among other things, explainablility for deep neural networks has been a topic of intensive research due to the meteoric rise in prominence of deep neural networks and their "black-box" nature. xAI approaches can be characterized along different dimensions such as their scope (global versus local explanations) or underlying methodologies (statistic-based versus rule-based strategies). Methods generating global explanations aim to provide reasoning process applicable to all possible output classes while local explanation methods focus only on a single, specific class. SHAP (SHapley Additive exPlanations), a well-known statistical technique, identifies important features of a network. Deep neural network rule extraction method constructs IF-THEN rules that link input conditions to a class. Another approach focuses on generating counterfactuals which help explain how small changes to an input can affect the model's predictions. However, these techniques primarily focus on the input-output relationship and thus neglect the structure of the network in explanation generation.   In this work, we propose xDNN(ASP), an explanation generation system for deep neural networks that provides global explanations. Given a neural network model and its training data, xDNN(ASP) extracts a logic program under answer set semantics that-in the ideal case-represents the trained model, i.e., answer sets of the extracted program correspond one-to-one to input-output pairs of the network. We demonstrate experimentally, using two synthetic datasets, that not only the extracted logic program maintains a high-level of accuracy in the prediction task, but it also provides valuable information for the understanding of the model such as the importance of features as well as the impact of hidden nodes on the prediction. The latter can be used as a guide for reducing the number of nodes used in hidden layers, i.e., providing a means for optimizing the network.


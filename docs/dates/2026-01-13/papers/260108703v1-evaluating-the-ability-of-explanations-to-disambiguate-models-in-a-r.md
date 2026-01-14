---
layout: default
title: Evaluating the Ability of Explanations to Disambiguate Models in a Rashomon Set
---

# Evaluating the Ability of Explanations to Disambiguate Models in a Rashomon Set
**arXiv**：[2601.08703v1](https://arxiv.org/abs/2601.08703) · [PDF](https://arxiv.org/pdf/2601.08703.pdf)  
**作者**：Kaivalya Rawal, Eoin Delaney, Zihao Fu, Sandra Wachter, Chris Russell  

**一句话要点**：提出AXE方法以评估Rashomon集合中模型解释的区分能力

**关键词**：可解释人工智能, Rashomon集合, 解释评估, 特征重要性, 对抗性公平清洗

## 3 点简述
- 核心问题：解释性AI中，Rashomon集合内模型行为差异被传统评估方法掩盖
- 方法要点：基于三项原则设计AXE方法，评估特征重要性解释，无需真实解释
- 实验或效果：AXE能100%检测对抗性公平清洗，并识别受保护属性的使用

## 摘要（原文）

> Explainable artificial intelligence (XAI) is concerned with producing explanations indicating the inner workings of models. For a Rashomon set of similarly performing models, explanations provide a way of disambiguating the behavior of individual models, helping select models for deployment. However explanations themselves can vary depending on the explainer used, and need to be evaluated. In the paper "Evaluating Model Explanations without Ground Truth", we proposed three principles of explanation evaluation and a new method "AXE" to evaluate the quality of feature-importance explanations. We go on to illustrate how evaluation metrics that rely on comparing model explanations against ideal ground truth explanations obscure behavioral differences within a Rashomon set. Explanation evaluation aligned with our proposed principles would highlight these differences instead, helping select models from the Rashomon set. The selection of alternate models from the Rashomon set can maintain identical predictions but mislead explainers into generating false explanations, and mislead evaluation methods into considering the false explanations to be of high quality. AXE, our proposed explanation evaluation method, can detect this adversarial fairwashing of explanations with a 100% success rate. Unlike prior explanation evaluation strategies such as those based on model sensitivity or ground truth comparison, AXE can determine when protected attributes are used to make predictions.


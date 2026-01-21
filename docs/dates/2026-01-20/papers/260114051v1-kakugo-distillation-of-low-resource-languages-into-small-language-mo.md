---
layout: default
title: Kakugo: Distillation of Low-Resource Languages into Small Language Models
---

# Kakugo: Distillation of Low-Resource Languages into Small Language Models
**arXiv**：[2601.14051v1](https://arxiv.org/abs/2601.14051) · [PDF](https://arxiv.org/pdf/2601.14051.pdf)  
**作者**：Peter Devine, Mardhiyah Sanni, Farid Adilazuarda, Julieta Gil Loizaga, Barry Haddow  

**一句话要点**：提出Kakugo管道，以低成本训练低资源语言的小型语言模型

**关键词**：低资源语言, 小型语言模型, 知识蒸馏, 合成数据生成, 多语言NLP, 成本效益

## 3 点简述
- 核心问题：低资源语言缺乏训练数据，难以开发通用AI模型。
- 方法要点：使用大教师模型生成合成提示和翻译指令数据集，构建训练数据。
- 实验或效果：在54种语言上评估，模型在翻译、分类等任务中性能提升，单语言成本低于50美元。

## 摘要（原文）

> We present Kakugo, a novel and cost-effective pipeline designed to train general-purpose Small Language Models (SLMs) for low-resource languages using only the language name as input. By using a large teacher model to generate synthetic prompts and translate instruction datasets, we produced training data and SLMs for 54 low-resource languages. Evaluations across a diverse set of general natural language processing tasks, including translation, classification, and question answering, demonstrate that our pipeline consistently improves performance over base models. With a total generation and training cost of under $50 per language, Kakugo offers an accessible method for communities to develop language-specific AI.


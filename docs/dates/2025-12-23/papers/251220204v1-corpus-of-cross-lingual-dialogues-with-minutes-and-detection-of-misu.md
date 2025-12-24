---
layout: default
title: Corpus of Cross-lingual Dialogues with Minutes and Detection of Misunderstandings
---

# Corpus of Cross-lingual Dialogues with Minutes and Detection of Misunderstandings
**arXiv**：[2512.20204v1](https://arxiv.org/abs/2512.20204) · [PDF](https://arxiv.org/pdf/2512.20204.pdf)  
**作者**：Marko Čechovič, Natália Komorníková, Dominik Macháček, Ondřej Bojar  

**一句话要点**：提出跨语言对话语料库与误解检测方法，以评估自动语音翻译系统。

**关键词**：跨语言对话语料库, 自动语音翻译, 误解检测, 大语言模型评估, 会议纪要生成

## 3 点简述
- 核心问题：缺乏多语言会议场景的评估语料库，需支持跨语言对话研究。
- 方法要点：构建包含12种语言录音、转录、翻译及会议纪要的5小时语料库。
- 实验或效果：手动标注误解，测试大语言模型检测能力，Gemini模型召回率77%、精确率47%。

## 摘要（原文）

> Speech processing and translation technology have the potential to facilitate meetings of individuals who do not share any common language. To evaluate automatic systems for such a task, a versatile and realistic evaluation corpus is needed. Therefore, we create and present a corpus of cross-lingual dialogues between individuals without a common language who were facilitated by automatic simultaneous speech translation. The corpus consists of 5 hours of speech recordings with ASR and gold transcripts in 12 original languages and automatic and corrected translations into English. For the purposes of research into cross-lingual summarization, our corpus also includes written summaries (minutes) of the meetings.
>   Moreover, we propose automatic detection of misunderstandings. For an overview of this task and its complexity, we attempt to quantify misunderstandings in cross-lingual meetings. We annotate misunderstandings manually and also test the ability of current large language models to detect them automatically. The results show that the Gemini model is able to identify text spans with misunderstandings with recall of 77% and precision of 47%.


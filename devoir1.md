# Devoir 1

![](https://www.seeklogo.net/wp-content/uploads/2016/09/facebook-icon-preview-1-400x400.png)

Pour ce premier devoir, je vous fournis un fichier à partir duquel vous devrez travailler. C'est [devoir1.py](devoir1.py) que vous pouvez copier-coller dans Sublime&nbsp;Text. Vous pouvez aussi le télécharger pour ensuite l'ouvrir avec Sublime&nbsp;Text.

Vous constaterez qu'il s'agit d'un début de script python qui ne contient pour l'instant qu'une variable appelée **_publications_**.

Cette variable est en fait une liste contenant elle-même 3&nbsp;260 listes.

Chacune de ces listes contient de l'information sur une publication (*«post»*) faite sur Facebook par un média québécois en 2017. L'ensemble représente un échantillon de 5% des publications réelles des 101 médias québécois les plus «aimés» sur Facebook.

Pour chaque *«post»*, il y a:

- Le nom du média qui l'a publié.
- Sa date de publication.
- Son numéro d'identification unique.
- Le nombre de fois où il a été **partagé**.
- Le nombre de **réactions** qu'il a suscité («j'aime», «love», «haha», etc.).
- Le nombre de **commentaires** qu'il a provoqué.

Si on considère que l'**engagement** sur un *«post»* est la somme des partages, des réactions et des commentaires, écrivez un script qui calcule l'engagement total de chaque média. Il faut donc que votre script écrive, dans le terminal, une phrase par média (101 phrases au total, donc), phrase qui devra ressembler à quelque chose comme:

```Les publications du média X ont été partagées X fois, ont provoqué X réactions et ont généré X commentaires, pour un engagement total de X en 2017.```

Vous vous rendrez compte qu'il y a une difficulté dans ce devoir: comment compter les données pour chacun des médias?

Je vous suggère de commencer par écrire un premier script qui compte le nombre de partages, de réactions, de commentaires ainsi que l'engagement **POUR L'ENSEMBLE** des 101 médias de cet échantillon. Comme je l'explique dans [mes critères d'évaluation](travaux.md#mes-critères-dévaluation), si vous remettez un script qui fait cela, je considérerais qu'il s'agit d'un effort qui vaut un B, voire un B+.

Essayez ensuite de voir comment faire pour les compter pour chaque média individuellement.

N'oubliez pas de mettre votre script, une fois que vous l'aurez complété, dans un répertoire sur votre compte Github, répertoire que vous appellerez **EDM5240-devoir1** avant l'[heure de tombée](travaux.md#devoir-1---lengagement-des-médias-québécois-sur-facebook).

Bonne chance!

<hr>

Si vous souhaitez faire un deuxième exercice, vous pouvez tenter de faire [le devoir 1 de l'hiver 2017](https://github.com/jhroy/syllabus-edm5240-H2017/blob/master/devoir1.md) qui consiste à générer les numéros de permis du collège des médecins à partir de 2017 et de reculer jusqu'en 1930.

Vous pouvez consulter [les solutions proposées par les étudiants](https://github.com/Journalisme-UQAM?utf8&q=devoir-1) (et les corrigés qu'elles contiennent).

Vous pouvez également voir [le code que j'ai présenté en classe](mdNumPermis.py) pour générer ces numéros de permis.
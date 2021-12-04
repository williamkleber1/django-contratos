# Generated by Django 3.2.9 on 2021-12-04 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_contrato', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('objeto', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Contratos',
                'db_table': 'Contratos',
                'ordering': ['ano'],
            },
        ),
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_fornecedor', models.AutoField(primary_key=True, serialize=False)),
                ('razao_social', models.CharField(max_length=60)),
                ('cnpj', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('telefone', models.CharField(blank=True, max_length=12, null=True)),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedores_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Fornecedores',
                'db_table': 'Fornecedores',
                'ordering': ['razao_social'],
            },
        ),
        migrations.CreateModel(
            name='NaturezasDespesa',
            fields=[
                ('id_natureza_despesa', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_natureza_despesas', models.CharField(max_length=8)),
                ('desc_natureza_despesa', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'Naturezas Despesas',
                'db_table': 'NaturezasDespesa',
                'ordering': ['desc_natureza_despesa'],
            },
        ),
        migrations.CreateModel(
            name='Vigencias',
            fields=[
                ('id_vigencia', models.AutoField(primary_key=True, serialize=False)),
                ('dt_inicio_vigencia', models.DateField()),
                ('dt_fim_vigencia', models.DateField()),
                ('id_contrato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='suprimentos.contratos')),
            ],
            options={
                'verbose_name_plural': 'Vigencias',
                'db_table': 'Vigencias',
                'ordering': ['id_contrato'],
            },
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('id_projeto', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('dt_inicio_vigencia', models.DateField()),
                ('dt_fim_vigencia', models.DateField()),
                ('dt_alt', models.DateField()),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projetos_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Projetos',
                'db_table': 'Projetos',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Ordens',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_ordem', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('id_fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ordens', to='suprimentos.fornecedores')),
                ('id_natureza_despesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ordens', to='suprimentos.naturezasdespesa')),
                ('id_projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ordens', to='suprimentos.projetos')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordens_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ordens',
                'db_table': 'Ordens',
                'ordering': ['ano'],
            },
        ),
        migrations.CreateModel(
            name='ItensOrdem',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_item_ordem', models.AutoField(primary_key=True, serialize=False)),
                ('produto_servico', models.CharField(max_length=150)),
                ('qtd', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('vinculado', models.BooleanField(default=False)),
                ('id_ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suprimentos.ordens')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itensordem_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itensordem_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Itens Ordem',
                'db_table': 'ItensOrdem',
                'ordering': ['produto_servico'],
            },
        ),
        migrations.CreateModel(
            name='ItensContratos',
            fields=[
                ('dt_cad', models.DateField(auto_now_add=True)),
                ('dt_alt', models.DateField(auto_now=True, null=True)),
                ('id_item_contrato', models.AutoField(primary_key=True, serialize=False)),
                ('qtd', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('id_contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suprimentos.contratos')),
                ('id_item_ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suprimentos.itensordem')),
                ('id_user_alt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itenscontratos_user_alt', to=settings.AUTH_USER_MODEL)),
                ('id_user_cad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itenscontratos_user_cad', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Itens Contratos',
                'db_table': 'ItensContratos',
                'ordering': ['id_contrato'],
            },
        ),
        migrations.AddField(
            model_name='contratos',
            name='id_prestador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contratos', to='suprimentos.fornecedores'),
        ),
        migrations.AddField(
            model_name='contratos',
            name='id_user_alt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contratos_user_alt', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contratos',
            name='id_user_cad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contratos_user_cad', to=settings.AUTH_USER_MODEL),
        ),
    ]